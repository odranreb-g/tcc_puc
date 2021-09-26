import uuid

from django.db import models
from model_utils.models import TimeFramedModel


class DeliveryStatusChoices(models.TextChoices):
    IN_TRANSIT = "IN_TRANSIT", "IN_TRANSIT"
    DONE = "DONE", "DONE"


class Delivery(TimeFramedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_name = models.CharField("sender_name", max_length=100)
    sender_address = models.CharField("sender_address", max_length=100)
    sender_city = models.CharField("sender_city", max_length=50)
    sender_postal_code = models.CharField("sender_city", max_length=10)

    receiver_name = models.CharField("receiver_name", max_length=100)
    receiver_address = models.CharField("receiver_address", max_length=100)
    receiver_city = models.CharField("receiver_city", max_length=50)
    receiver_postal_code = models.CharField("receiver_city", max_length=10)

    freight_price = models.DecimalField("freight_price", max_digits=5, decimal_places=2)

    expected_delivery_date = models.DateTimeField(
        "expected_delivery_date", auto_now=False, auto_now_add=False
    )
    delivery_date = models.DateTimeField("delivery_date", auto_now=False, auto_now_add=False)

    status = models.CharField(
        "status",
        max_length=50,
        choices=DeliveryStatusChoices.choices,
        default=DeliveryStatusChoices.IN_TRANSIT,
    )

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"
