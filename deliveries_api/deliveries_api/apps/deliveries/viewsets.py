from rest_framework import viewsets

from apps.deliveries.models import Delivery
from apps.deliveries.serializers import DeliverySerializer


class DeliveryViewSet(viewsets.ModelViewSet):

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
