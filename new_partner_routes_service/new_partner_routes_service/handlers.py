import logging
from datetime import datetime, timezone
from http import HTTPStatus

import requests
from prettyconf import config
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from database import engine
from models import PartnerRoute

logger = logging.getLogger(__name__)

SESSION_MAKER = sessionmaker(bind=engine)


class NewPartnerRoutesHandler:
    def _delete_new_partner_route(self, new_route_uuid):
        response = requests.delete(
            f"{config('PARTNER_ROUTES_API')}/new-routes/{new_route_uuid}/",
            headers={"Content-Type": "application/json"},
        )

        if response.status_code == HTTPStatus.NO_CONTENT:
            logger.info("New Partner Route Deleted")
        else:
            logger.info(f"Fail Partner Route Deleted {response.json()}")
            raise Exception("Unprocessed msg.")

    def _insert_legacy_database(self, message):

        with SESSION_MAKER() as session:
            dt = datetime.now(timezone.utc)

            partner_route = PartnerRoute()
            partner_route.created = dt
            partner_route.modified = dt
            partner_route.price = message.get("price")
            partner_route.start_place = message.get("start_place")
            partner_route.finish_place = message.get("finish_place")
            partner_route.partner_id = message.get("partner_id")
            partner_route.status = message.get("status")

            session.add(partner_route)
            try:
                session.commit()
                logger.info("New route added.")
            except IntegrityError as error:
                logger.info(f"IntegrityError {error!r}")

    def process(self, message):
        self._insert_legacy_database(message)
        self._delete_new_partner_route(message.get("id"))
