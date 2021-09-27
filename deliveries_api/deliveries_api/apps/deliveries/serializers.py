from rest_framework import serializers

from apps.deliveries.models import Delivery


class DeliverySerializer(serializers.ModelSerializer):
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
            "type",
            "status",
            "partner_id",
        ]
