import requests
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.base import TemplateView
from prettyconf import config

from tests.factories import DeliveryFactory

from .forms import DeliveryForm, DeliveryUpdateForm
from .models import Delivery, PartnerRoute


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"editable_fields": ["status"]})

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"show_save_button": True})
        return context


class DeliveriesDetailView(UpdateView):
    model = Delivery
    form_class = DeliveryUpdateForm
    template_name = "deliveries/delivery_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = f"{config('DELIVERIES_API')}/deliveries/{self.object.id}"
        delivery = requests.get(url, headers={"Authorization": config("API_TOKEN")}).json() or {}

        context.update({"show_save_button": False, "zpl": (delivery.get("zpl") or {}).get("url")})
        return context


class PartnerRouteListView(ListView):
    template_name = "partner_routes/list.html"
    paginate_by = 30
    model = PartnerRoute

    def get_queryset(self):
        queryset = super().get_queryset()

        if qPartner := self.request.GET.get("qPartner"):
            queryset = queryset.filter(partner=qPartner)
        if qSender := self.request.GET.get("qSender"):
            queryset = queryset.filter(start_place=qSender)
        if qReceiver := self.request.GET.get("qReceiver"):
            queryset = queryset.filter(finish_place=qReceiver)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(PartnerRouteListView, self).get_context_data(**kwargs)
        context["qPartner"] = self.request.GET.get("qPartner", "").strip()
        context["qSender"] = self.request.GET.get("qSender", "").strip()
        context["qReceiver"] = self.request.GET.get("qReceiver", "").strip()
        return context
