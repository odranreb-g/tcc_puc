import json
import logging
import sys

import requests
from kafka import KafkaConsumer
from prettyconf import config

from handlers import PoolPartnerPriceHandler

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
root.addHandler(handler)
logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    config("KAFKA_TOPIC"),
    group_id=config("KAFKA_CONSUMER_GROUP"),
    bootstrap_servers=config("KAFKA_BOOTSTRAP_SERVERS", cast=config.list),
    value_deserializer=lambda m: json.loads(m.decode("ascii")),
)

handler = PoolPartnerPriceHandler()

if __name__ == "__main__":
    for message in consumer:
        try:
            handler.process(message.value.get("id"))
        except requests.exceptions.ConnectionError as error:
            logger.info(f"Error {error}")
