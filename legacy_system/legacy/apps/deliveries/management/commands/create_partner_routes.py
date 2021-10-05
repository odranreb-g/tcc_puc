import random

from apps.deliveries.models import PartnerRoute
from django.core.management.base import BaseCommand
from tests.factories import CITIES, PartnerFactory


class Command(BaseCommand):
    help = "Create Partner Routes"

    def handle(self, *args, **options):
        partner = PartnerFactory()

        for city_from in CITIES:
            for city_to in CITIES:
                if city_from == city_to:
                    continue

                PartnerRoute.objects.create(
                    start_place=city_from,
                    finish_place=city_to,
                    price=random.uniform(10, 100),
                    partner=partner,
                )

                self.stdout.write(self.style.SUCCESS(f"Route {city_from} -> {city_to} created."))
        self.stdout.write(self.style.SUCCESS("Every route created."))
