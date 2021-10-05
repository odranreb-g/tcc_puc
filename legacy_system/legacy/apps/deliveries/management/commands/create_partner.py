from django.core.management.base import BaseCommand
from tests.factories import PartnerFactory


class Command(BaseCommand):
    help = "Create Partner"

    def handle(self, *args, **options):
        partner = PartnerFactory()

        self.stdout.write(self.style.SUCCESS(f"Partner {partner.id} created."))
