import random

import factory

factory.Faker._DEFAULT_LOCALE = "pt-BR"


CITIES = [
    "Belo Horizonte",
    "Vespasiano",
    "Manhuaçu",
    "João Monlevade",
    "Contagem",
    "Sete Lagoas",
    "Ipatinga",
    "Reduto",
    "Realeza",
]

CITIES = random.sample(CITIES, len(CITIES))
CITIES_SHUFFLED = random.sample(CITIES, len(CITIES))


class NewRouteCreatedByPartnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "routes.NewRouteCreatedByPartner"

    start_place = factory.Iterator(CITIES)
    finish_place = factory.Iterator(CITIES_SHUFFLED)
    price = random.uniform(10, 100)
    partner_id = factory.Faker("uuid4")
