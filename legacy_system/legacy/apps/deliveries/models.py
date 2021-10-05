import uuid

from django.db import models
from model_utils.models import TimeStampedModel


class PartnerStatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "ACTIVE"
    INACTIVE = "INACTIVE", "INACTIVE"


class Partner(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("name", max_length=100)
    status = models.CharField(
        "status",
        max_length=8,
        choices=PartnerStatusChoices.choices,
        default=PartnerStatusChoices.ACTIVE,
    )

    class Meta:
        verbose_name = "Patner"
        verbose_name_plural = "Patners"


class RouteStatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "ACTIVE"
    INACTIVE = "INACTIVE", "INACTIVE"


class PartnerRoute(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_place = models.CharField("start_place", max_length=50)
    finish_place = models.CharField("finish_place", max_length=50)
    price = models.DecimalField("price", max_digits=5, decimal_places=2)
    partner = models.ForeignKey(Partner, on_delete=models.DO_NOTHING)
    status = models.CharField(
        "status",
        max_length=10,
        choices=RouteStatusChoices.choices,
        default=RouteStatusChoices.ACTIVE,
    )

    class Meta:
        verbose_name = "PartnerRoute"
        verbose_name_plural = "PartnerRoutes"
        unique_together = [["start_place", "finish_place", "partner_id"]]


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

    freight_price = models.DecimalField("freight_price", max_digits=5, decimal_places=2, null=True)

    expected_delivery_date = models.DateField("expected_delivery_date", auto_now=False, auto_now_add=False)
    delivery_date = models.DateField("delivery_date", auto_now=False, auto_now_add=False, null=True)

    type = models.CharField(
        "type", max_length=9, choices=DeliveryTypeChoices.choices, default=DeliveryTypeChoices.QUOTATION
    )

    status = models.CharField(
        "status",
        max_length=10,
        choices=DeliveryStatusChoices.choices,
        default=DeliveryStatusChoices.QUOTATION,
    )
    partner_route = models.ForeignKey(PartnerRoute, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"
