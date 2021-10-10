from rest_framework import filters, viewsets

from apps.deliveries.models import Delivery
from apps.deliveries.serializers import DeliverySerializer


class DeliveryViewSet(viewsets.ModelViewSet):

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["delivery_entry_modified", "delivery_entry_created"]
