from django.db import models


class Fuel(models.Model):
    type_fuel = models.CharField(max_length=50, unique=True)
    count_fuel = models.IntegerField(default=0, blank=True)
    price = models.FloatField(default=0.0)
    description = models.TextField(null=True, max_length=300)

