import json
import logging
import uuid

from deliveries_api.kafka_config import kafka_producer
from django.db import models
from model_utils.models import TimeStampedModel

logger = logging.getLogger(__name__)


class DeliveryStatusChoices(models.TextChoices):
    QUOTATION = "QUOTATION", "QUOTATION"
    IN_TRANSIT = "IN_TRANSIT", "IN_TRANSIT"
    DONE = "DONE", "DONE"


class DeliveryTypeChoices(models.TextChoices):
    QUOTATION = "QUOTATION", "QUOTATION"
    DELIVERY = "DELIVERY", "DELIVERY"


class Delivery(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_name = models.CharField("sender_name", max_length=100)
    sender_address = models.CharField("sender_address", max_length=100)
    sender_city = models.CharField("sender_city", max_length=50)
    sender_postal_code = models.CharField("sender_postal_code", max_length=10)

    receiver_name = models.CharField("receiver_name", max_length=100)
    receiver_address = models.CharField("receiver_address", max_length=100)
    receiver_city = models.CharField("receiver_city", max_length=50)
    receiver_postal_code = models.CharField("receiver_postal_code", max_length=10)

    freight_price = models.DecimalField("freight_price", max_digits=5, decimal_places=2)

    expected_delivery_date = models.DateField("expected_delivery_date", auto_now=False, auto_now_add=False)
    delivery_date = models.DateField("delivery_date", auto_now=False, auto_now_add=False, null=True)

    delivery_entry_created = models.DateTimeField()
    delivery_entry_modified = models.DateTimeField()

    type = models.CharField(
        "type", max_length=9, choices=DeliveryTypeChoices.choices, default=DeliveryTypeChoices.QUOTATION
    )

    status = models.CharField(
        "status",
        max_length=10,
        choices=DeliveryStatusChoices.choices,
        default=DeliveryStatusChoices.QUOTATION,
    )

    partner_id = models.UUIDField(null=True)

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"

    def save(self, *args, **kwargs):
        super(Delivery, self).save(*args, **kwargs)
        topic = f"{self.__class__.__name__.lower()}_{self.status.lower()}"
        kafka_producer.send(topic, {"id": str(self.id)})
        logger.info(f"Delivery {self.id} sent to topic {topic}.")
