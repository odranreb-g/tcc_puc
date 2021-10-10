import json

from kafka import KafkaProducer
from prettyconf import config

kafka_producer = KafkaProducer(
    bootstrap_servers=config("KAFKA_BOOTSTRAP_SERVERS", cast=config.list),
    value_serializer=lambda m: json.dumps(m).encode("ascii"),
)
