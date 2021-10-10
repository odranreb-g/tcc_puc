import uuid
from datetime import datetime

from apps.deliveries.models import Delivery, DeliveryStatusChoices
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "change delivery status to in_transit"

    def add_arguments(self, parser):
        parser.add_argument(
            "id",
            help="ID",
        )

    def handle(self, *args, **options):

        id = options.get("id")
        delivery = Delivery.objects.get(id=id)
        delivery.status = DeliveryStatusChoices.IN_TRANSIT
        delivery.modified = datetime.now()
        delivery.save()
        self.stdout.write(self.style.SUCCESS(f"Delivery {delivery.id} updated"))
