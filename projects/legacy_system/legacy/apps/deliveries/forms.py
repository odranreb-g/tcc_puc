from django.forms import DateField, DateInput, ModelForm

from .models import Delivery


class DeliveryForm(ModelForm):
    expected_delivery_date = DateField(widget=DateInput(attrs={"type": "date"}))

    class Meta:
        model = Delivery
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(DeliveryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
        self.fields["freight_price"].required = False
        self.fields["delivery_date"].required = False
        self.fields["partner_route"].required = False


class DeliveryUpdateForm(ModelForm):
    expected_delivery_date = DateField(widget=DateInput(attrs={"type": "date"}))

    class Meta:
        model = Delivery
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        editable_fields = kwargs.pop("editable_fields", [])

        super(DeliveryUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

        self.fields["freight_price"].required = False
        self.fields["delivery_date"].required = False
        self.fields["partner_route"].required = False

        for key, field in self.fields.items():
            if key not in editable_fields:
                field.disabled = True
