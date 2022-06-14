from rest_framework import serializers

from apis.models import ServiceAreas, GeoJson, Provider


class GeoJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoJson
        fields = "__all__"


class ServiceAreaSerializer(GeoJsonSerializer, serializers.ModelSerializer):
    polygon = GeoJsonSerializer()

    class Meta:
        model = ServiceAreas
        fields = ("polygon", "provider", "name", "price")


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"
