import json
import logging
import time
from abc import ABC, abstractmethod
from http import HTTPStatus

import requests
from prettyconf import config
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from database import engine
from models import Delivery, Route

logger = logging.getLogger(__name__)


class PoolingBase(ABC):
    _URL = None
    _CLASS_REF = None
    _FIELD_REF = None

    def __init__(self, session_maker):
        self._session_maker = session_maker

    @abstractmethod
    def get_last_entity(self):
        ...

    @abstractmethod
    def get_data_from_database(self, date):
        ...

    def process(self):
        try:
            logger.info(f"Pooling {self.__class__.__name__.lower()}")
            last_date = self.get_last_entity()
            logger.info(f"Pooling {self.__class__.__name__.lower()}: last_date{last_date}")
            objs = self.get_data_from_database(last_date)
            logger.info(f"Pooling {self.__class__.__name__.lower()}: objs{objs}")
            self.send_to_new_api(objs)
        except requests.exceptions.ConnectionError as error:
            logger.error(f"Error {error!r}")

    def send_to_new_api(self, objs):
        for index, obj in enumerate(objs):
            if obj.created == obj.modified:
                response = requests.post(self.URL, data=obj.to_dict(), headers={"x-pooling-system": "true"})
            else:
                response = requests.patch(
                    f"{self.URL}{obj.id}/",
                    data=obj.to_dict(),
                    headers={"x-pooling-system": "True"},
                )

            if response.status_code in [HTTPStatus.CREATED, HTTPStatus.OK]:
                print(f"{index+1}/{len(objs)} -> OK")
            else:
                print(f"{index+1}/{len(objs)} -> FAIL {response.json()}")


class DeliveriesPooling(PoolingBase):
    URL = f"{config('DELIVERIES_API')}/deliveries/"

    def get_last_entity(self):
        response = requests.get(
            self.URL,
            params={"ordering": "-delivery_entry_modified", "limit": 1},
        ).json()

        if response["results"]:
            return response["results"][0]["delivery_entry_modified"]
        else:
            return ""

    def get_data_from_database(self, date):
        with self._session_maker() as session:
            query = session.query(Delivery)
            if date:
                modified = date
                query = query.filter(func.date_trunc("second", Delivery.modified) > modified)

            return query.all()


class PartnerRoutesPooling(PoolingBase):
    URL = f"{config('PARTNER_ROUTES_API')}/routes/"

    def get_last_entity(self):
        response = requests.get(
            self.URL,
            params={"ordering": "-route_entry_modified", "limit": 1},
        ).json()

        if response["results"]:
            return response["results"][0]["route_entry_modified"]
        else:
            return ""

    def get_data_from_database(self, date):
        with self._session_maker() as session:
            query = session.query(Route)
            if date:
                updated = date
                query = query.filter(func.date_trunc("second", Route.modified) > updated)
            objs = query.all()
        return objs


class PoolingExecuter:
    _poolings = [DeliveriesPooling, PartnerRoutesPooling]
    _session_maker = sessionmaker(bind=engine)

    def process(self):
        self._poolings = [pooling(self._session_maker) for pooling in self._poolings]
        try:
            logger.info("starting pooling")
            for pooling in self._poolings:
                pooling.process()
            logger.info("finished pooling")
        except json.decoder.JSONDecodeError as error:
            logger.error(f"error {error}")
