from rest_framework import serializers

from apps.routes.models import City, Route


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name"]


class RouteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    start_place = serializers.CharField()
    finish_place = serializers.CharField()

    class Meta:
        model = Route
        fields = [
            "id",
            "price",
            "start_place",
            "finish_place",
            "partner_id",
            "status",
            "route_entry_created",
            "route_entry_modified",
        ]

    def create(self, validated_data):
        start_place = validated_data.pop("start_place")
        finish_place = validated_data.pop("finish_place")

        route = Route.objects.create(
            **validated_data,
            start_place=City.objects.get_or_create(name=start_place)[0],
            finish_place=City.objects.get_or_create(name=finish_place)[0]
        )

        return route
