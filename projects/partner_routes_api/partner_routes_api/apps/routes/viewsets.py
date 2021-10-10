from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from apps.routes.models import NewRouteCreatedByPartner, Route
from apps.routes.serializers import NewRouteCreatedByPartnerSerializer, RouteSerializer


class RouteFilter(filters.FilterSet):
    start_place = filters.CharFilter(field_name="start_place__name")
    finish_place = filters.CharFilter(field_name="finish_place__name")

    class Meta:
        model = Route
        fields = ["start_place", "finish_place"]


class RouteViewSet(viewsets.ModelViewSet):

    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    ordering_fields = ["route_entry_modified"]
    filter_backends = (
        OrderingFilter,
        filters.DjangoFilterBackend,
    )
    filterset_class = RouteFilter


class NewRouteCreatedByPartnerViewSet(viewsets.ModelViewSet):

    queryset = NewRouteCreatedByPartner.objects.all()
    serializer_class = NewRouteCreatedByPartnerSerializer
