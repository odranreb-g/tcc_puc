"""deliveries_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from apps.deliveries import viewsets
from django import urls
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"deliveries", viewsets.DeliveryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Deliveries API",
        default_version="v1",
        description="Deliveries API - TFC PCC",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bgomesdeabreu@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# The API URLs are now determined automatically by the router.

urlpatterns = []

for prefix in ["", "deliveries-api/"]:
    urlpatterns.extend(
        [
            path(f"{prefix}admin/", admin.site.urls),
            path(
                f"{prefix}swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
            ),
            path(f"{prefix}redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
            path(f"{prefix}", include(router.urls)),
            path(f"{prefix}", include("django_prometheus.urls")),
        ]
    )
