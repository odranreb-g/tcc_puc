from rest_framework import filters, viewsets

from apps.routes.models import Route
from apps.routes.serializers import RouteSerializer


class RouteViewSet(viewsets.ModelViewSet):

    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["route_entry_modified"]
