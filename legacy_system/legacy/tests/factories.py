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

CITIES_SHUFFLED = random.sample(CITIES, len(CITIES))


class DeliveryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "deliveries.Delivery"

    sender_address = factory.Faker("street_address")
    sender_city = factory.Iterator(CITIES)
    sender_postal_code = factory.Faker("postcode")
    sender_name = factory.Faker("name")

    receiver_address = factory.Faker("street_address")
    receiver_city = factory.Iterator(CITIES_SHUFFLED)
    receiver_postal_code = factory.Faker("postcode")
    receiver_name = factory.Faker("name")
