import json
import logging
import sys
import sentry_sdk
from kafka import KafkaConsumer
from prettyconf import config

from handlers import ZPLGeneratorHandler

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
root.addHandler(handler)

sentry_sdk.init(
    "https://e1fc87c1991d412aad19dc812385c9a1@o89421.ingest.sentry.io/6000492",
    traces_sample_rate=1.0,
)


consumer = KafkaConsumer(
    config("KAFKA_TOPIC"),
    group_id=config("KAFKA_CONSUMER_GROUP"),
    bootstrap_servers=config("KAFKA_BOOTSTRAP_SERVERS", cast=config.list),
    value_deserializer=lambda m: json.loads(m.decode("ascii")),
)

handler = ZPLGeneratorHandler()

if __name__ == "__main__":
    for message in consumer:
        handler.process(message.value.get("id"))
