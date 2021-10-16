from django.urls import path

from apps.deliveries.views import (
    DeliveriesCreateView,
    DeliveriesDetailView,
    DeliveriesListView,
    DeliveriesUpdateView,
)

urlpatterns = [
    path("", DeliveriesListView.as_view(), name="list"),
    path("create/", DeliveriesCreateView.as_view(), name="create"),
    path("<uuid:pk>/editar", DeliveriesUpdateView.as_view(), name="update"),
    path("<uuid:pk>/detalhes", DeliveriesDetailView.as_view(), name="detail"),
]
