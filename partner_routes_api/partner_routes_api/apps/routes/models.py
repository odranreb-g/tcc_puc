import logging
import uuid

from django.db import models
from django.template.defaultfilters import slugify
from model_utils.models import TimeStampedModel
from partner_routes_api.kafka_config import kafka_producer
from simple_history.models import HistoricalRecords

logger = logging.getLogger(__name__)


class City(TimeStampedModel):
    name = models.CharField("name", max_length=50)
    slug = models.SlugField(null=False, unique=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class RouteStatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "ACTIVE"
    INACTIVE = "INACTIVE", "INACTIVE"


class Route(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField("price", max_digits=5, decimal_places=2)
    start_place = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name="start_place")
    finish_place = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name="finish_place")
    partner_id = models.UUIDField()
    status = models.CharField(
        "status",
        max_length=10,
        choices=RouteStatusChoices.choices,
        default=RouteStatusChoices.ACTIVE,
    )
    history = HistoricalRecords()

    route_entry_created = models.DateTimeField()
    route_entry_modified = models.DateTimeField()

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"
        unique_together = [["start_place", "finish_place", "partner_id"]]


class NewRouteCreatedByPartner(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField("price", max_digits=5, decimal_places=2)
    start_place = models.CharField("start_place", max_length=50)
    finish_place = models.CharField("finish_place", max_length=50)
    partner_id = models.UUIDField()
    status = models.CharField(
        "status",
        max_length=10,
        choices=RouteStatusChoices.choices,
        default=RouteStatusChoices.ACTIVE,
    )

    prefix_topic = "new_route_created_by_partner"

    class Meta:
        verbose_name = "NewRouteCreatedByPartner"
        verbose_name_plural = "NewRoutesCreatedByPartner"
        unique_together = [["start_place", "finish_place", "partner_id"]]

    def save(self, *args, **kwargs):
        super(NewRouteCreatedByPartner, self).save(*args, **kwargs)

        from apps.routes.serializers import NewRouteCreatedByPartnerSerializer

        serializer = NewRouteCreatedByPartnerSerializer(self)
        topic = f"{self.prefix_topic}_{self.status.lower()}"
        kafka_producer.send(topic, serializer.data)
        kafka_producer.flush()
        logger.info(f"NewRouteCreatedByPartner {self.id} sent to topic {topic}.")
