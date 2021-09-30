import json

from kafka import KafkaConsumer
from prettyconf import config

from zpl_generate import ZPLGenerator

consumer = KafkaConsumer(
    config("KAFKA_TOPIC"),
    group_id=config("KAFKA_CONSUMER_GROUP"),
    bootstrap_servers=config("KAFKA_BOOTSTRAP_SERVERS", cast=config.list),
    value_deserializer=lambda m: json.loads(m.decode("ascii")),
)

zpl_generator = ZPLGenerator()
if __name__ == "__main__":
    for message in consumer:
        path = zpl_generator.process(message.value.get("id"))
        # TODO UPDATE DELIVERY WITH ZPL
        print(path)
