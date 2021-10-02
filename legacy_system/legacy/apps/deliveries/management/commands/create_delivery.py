import random
import time
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from tests.factories import DeliveryFactory


class Command(BaseCommand):
    help = "Create deliveries"

    def add_arguments(self, parser):
        parser.add_argument(
            "--multiples_qty",
            help="Create multiples deliveries",
            type=int,
        )

    def handle(self, *args, **options):

        qty = options.get("multiples_qty") or 1

        for index in range(qty):
            delivery = DeliveryFactory(
                expected_delivery_date=datetime.now() + timedelta(days=random.uniform(1, 30)),
            )

            self.stdout.write(self.style.SUCCESS(f"Delivery {delivery.id} created {index + 1} / {qty}"))
            time.sleep(1)
