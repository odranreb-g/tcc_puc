import uuid

from django.db import models
from model_utils.models import TimeFramedModel


class DeliveryStatusChoices(models.TextChoices):
    IN_TRANSIT = "IN_TRANSIT", "IN_TRANSIT"
    DONE = "DONE", "DONE"


class DeliveryTypeChoices(models.TextChoices):
    QUOTATION = "QUOTATION", "QUOTATION"
    DELIVERY = "DELIVERY", "DELIVERY"


class Delivery(TimeFramedModel):
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

    type = models.CharField(
        "type", max_length=9, choices=DeliveryTypeChoices.choices, default=DeliveryTypeChoices.QUOTATION
    )

    status = models.CharField(
        "status",
        max_length=10,
        choices=DeliveryStatusChoices.choices,
        default=DeliveryStatusChoices.IN_TRANSIT,
    )

    partner_id = models.UUIDField(null=True)

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"
