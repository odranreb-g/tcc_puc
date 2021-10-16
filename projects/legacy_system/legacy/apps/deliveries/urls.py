from django.urls import path

from apps.deliveries.views import DeliveriesCreateView, DeliveriesListView, DeliveriesUpdateView

urlpatterns = [
    path("", DeliveriesListView.as_view(), name="list"),
    path("create/", DeliveriesCreateView.as_view(), name="create"),
    path("<uuid:pk>/", DeliveriesUpdateView.as_view(), name="update"),
]
