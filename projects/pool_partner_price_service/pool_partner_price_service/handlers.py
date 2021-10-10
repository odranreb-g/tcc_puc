import json
import logging
from datetime import datetime, timezone
from http import HTTPStatus

import requests
from prettyconf import config
from sqlalchemy.orm import sessionmaker

from database import engine
from models import Delivery

logger = logging.getLogger(__name__)

SESSION_MAKER = sessionmaker(bind=engine)


class PoolPartnerPriceHandler:
    def _get_delivery(self, delivery_uuid):
        return requests.get(f"{config('DELIVERIES_API')}/deliveries/{delivery_uuid}/").json()

    def _get_routes(self, delivery):
        return requests.get(
            f"{config('PARTNER_ROUTES_API')}/routes/?start_place={delivery.get('sender_city')}"
            f"&finish_place={delivery.get('receiver_city')}"
        ).json()["results"]

    def _get_min_route(self, routes):
        return min(routes, key=lambda i: i.get("price"))

    def _update_delivery(self, delivery_uuid, route_uuid, price):
        response = requests.patch(
            f"{config('DELIVERIES_API')}/deliveries/{delivery_uuid}/",
            data=json.dumps({"partner_route_id": route_uuid, "freight_price": price}),
            headers={"Content-Type": "application/json"},
        )

        if response.status_code == HTTPStatus.OK:
            logger.info("Delivery Updated")
        else:
            logger.info(f"Fail Delivery Updated {response.json()}")
            raise Exception("Unprocessed msg.")

    def _update_legacy_database(self, delivery_uuid, route_uuid, price):

        with SESSION_MAKER() as session:
            dt = datetime.now(timezone.utc)
            session.query(Delivery).filter(Delivery.id == delivery_uuid).update(
                {"freight_price": price, "partner_route_id": route_uuid, "modified": dt}
            )
            session.commit()

    def process(self, uuid):
        delivery = self._get_delivery(uuid)
        routes = self._get_routes(delivery)
        min_route = self._get_min_route(routes)
        self._update_delivery(uuid, min_route.get("id"), min_route.get("price"))
        self._update_legacy_database(uuid, min_route.get("id"), min_route.get("price"))
