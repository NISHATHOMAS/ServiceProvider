from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    country_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    language = models.CharField(max_length=32)
    currency = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)


class GeoJson(models.Model):
    vertex = models.CharField(max_length=16)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class ServiceAreas(models.Model):
    provider = models.ForeignKey(Provider,
                                 on_delete=models.CASCADE,
                                 related_name="service_provider")
    name = models.CharField(max_length=64)
    price = models.FloatField(default=0.00)
    polygon = models.ForeignKey(GeoJson,
                                on_delete=models.CASCADE,
                                related_name="polygon_coordinates")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
