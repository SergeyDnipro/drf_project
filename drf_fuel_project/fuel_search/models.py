from django.db import models


# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, max_length=300)


class GasStation(models.Model):
    location = models.CharField(max_length=50)
    description = models.TextField(null=True, max_length=300)
    url = models.URLField(max_length=200)


class Fuel(models.Model):
    type_fuel = models.CharField(max_length=50, unique=True)
    count_fuel = models.IntegerField(default=0, blank=True)
    price = models.FloatField(default=0.0)
    delivered_at = models.DateTimeField(auto_now_add=True, blank=True)
