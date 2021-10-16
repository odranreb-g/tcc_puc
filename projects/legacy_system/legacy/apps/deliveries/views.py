from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.base import TemplateView

from tests.factories import DeliveryFactory

from .forms import DeliveryForm, DeliveryUpdateForm
from .models import Delivery


class CustomLoginView(LoginView):
    template_name = "site/login.html"
    extra_context = {"next": "www.google.com.br"}


class DashboardView(TemplateView):
    template_name = "site/dashboard.html"


class DeliveriesListView(ListView):
    paginate_by = 30
    model = Delivery


class DeliveriesCreateView(CreateView):
    form_class = DeliveryForm
    template_name = "deliveries/delivery_form.html"

    success_url = reverse_lazy("deliveries:list")

    def get_initial(self):
        delivery = DeliveryFactory.build()
        return delivery.__dict__


class DeliveriesUpdateView(UpdateView):
    model = Delivery
    form_class = DeliveryUpdateForm
    template_name = "deliveries/delivery_form.html"

    success_url = reverse_lazy("deliveries:list")
