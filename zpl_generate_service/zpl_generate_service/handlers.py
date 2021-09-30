import json
import logging
from http import HTTPStatus

import requests
from prettyconf import config

from zpl_generate import ZPLGenerator

logger = logging.getLogger(__name__)


class ZPLGeneratorHandler:
    def __init__(self):
        self.zpl_generator = ZPLGenerator()

    def _update_delivery_with_zpl(self, uuid, path):
        url = f"{config('DELIVERIES_API')}/deliveries/{uuid}/"
        response = requests.patch(
            url, data=json.dumps({"zpl": {"url": path}}), headers={"Content-Type": "application/json"}
        )
        if response.status_code == HTTPStatus.OK:
            logger.info("Processed OK")
        else:
            logger.info(f"Fail Unprocessed {response.json()}")
            raise Exception("Unprocessed msg.")

    def process(self, uuid):
        path = self.zpl_generator.process(uuid)
        self._update_delivery_with_zpl(uuid, path)
