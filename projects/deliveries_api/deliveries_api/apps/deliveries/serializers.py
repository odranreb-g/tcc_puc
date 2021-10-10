from rest_framework import serializers

from apps.deliveries.models import ZPL, Delivery, DeliveryStatusChoices


class ZPLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZPL
        fields = ["url"]


class DeliverySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    zpl = ZPLSerializer(allow_null=True, required=False)

    class Meta:
        model = Delivery
        fields = [
            "id",
            "sender_name",
            "sender_address",
            "sender_city",
            "sender_postal_code",
            "receiver_name",
            "receiver_address",
            "receiver_city",
            "receiver_postal_code",
            "freight_price",
            "expected_delivery_date",
            "delivery_date",
            "status",
            "partner_route_id",
            "delivery_entry_created",
            "delivery_entry_modified",
            "zpl",
        ]

    def create(self, validated_data):
        validated_data.pop("zpl", None)
        delivery = Delivery.objects.create(**validated_data)
        return delivery

    def update(self, instance, validated_data):
        if "X-Pooling-System" in self.context["request"].headers:
            if validated_data["status"] == DeliveryStatusChoices.IN_TRANSIT.name:
                instance.status = DeliveryStatusChoices.PLP_PROCESS
            instance.delivery_entry_modified = validated_data.get("delivery_entry_modified")
            instance.save()
            return instance

        zpl = validated_data.pop("zpl", None)

        if instance.status == DeliveryStatusChoices.PLP_PROCESS.name and zpl:
            if instance.zpl is None:
                instance.zpl = ZPL.objects.create(**zpl)
            else:
                instance.zpl.url = zpl.get("url")
                instance.zpl.save()

        if instance.status == DeliveryStatusChoices.QUOTATION:
            instance.freight_price = validated_data.get("freight_price")
            instance.partner_route_id = validated_data.get("partner_route_id")

        instance.status = validated_data.get("status", instance.status)
        instance.save()

        return instance
