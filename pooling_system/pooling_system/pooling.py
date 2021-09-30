import logging
import time
from http import HTTPStatus

import requests
from prettyconf import config
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from database import engine
from models import Delivery

logger = logging.getLogger(__name__)


def delivies_pooling():
    try:
        response = requests.get(
            f"{config('DELIVERIES_API')}/deliveries/",
            params={"ordering": "-delivery_entry_created", "limit": 1},
        ).json()

        Session = sessionmaker(bind=engine)
        with Session() as session:
            query = session.query(Delivery)
            if response:
                created = response["results"][0]["delivery_entry_created"]
                query = query.filter(func.date_trunc("second", Delivery.created) > created)

            objs = query.all()

        for index, obj in enumerate(objs):
            response = requests.post(f"{config('DELIVERIES_API')}/deliveries/", data=obj.to_dict())
            if response.status_code == HTTPStatus.CREATED:
                print(f"{index+1}/{len(objs)} -> OK")
            else:
                print(f"{index+1}/{len(objs)} -> FAIL {response.json()}")

    except requests.exceptions.ConnectionError as error:
        logger.error(f"Error {error!r}")


def pooling():
    while True:
        print("starting pooling")
        delivies_pooling()
        print("finished pooling")
        time.sleep(10)
