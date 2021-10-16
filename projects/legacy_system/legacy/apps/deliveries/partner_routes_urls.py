from django.urls import path

from apps.deliveries.views import PartnerRouteListView

urlpatterns = [
    path("", PartnerRouteListView.as_view(), name="list"),
]
