import factory


class DeliveryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "deliveries.Delivery"
