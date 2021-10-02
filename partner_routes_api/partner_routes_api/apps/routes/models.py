import uuid

from django.db import models
from django.template.defaultfilters import slugify
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords


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
