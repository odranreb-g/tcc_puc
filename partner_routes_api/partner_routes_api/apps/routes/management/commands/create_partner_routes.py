from django.core.management.base import BaseCommand
from tests.factories import NewRouteCreatedByPartnerFactory


class Command(BaseCommand):
    help = "Create Partner Routes"

    def add_arguments(self, parser):
        parser.add_argument(
            "partner_id",
            help="Partner ID",
        )

    def handle(self, *args, **options):
        partner_id = options.get("partner_id")
        new_route = NewRouteCreatedByPartnerFactory(
            partner_id=partner_id, start_place="Reduto", finish_place="Manhuaçu"
        )

        self.stdout.write(self.style.SUCCESS(f"Route {new_route.id} created."))
