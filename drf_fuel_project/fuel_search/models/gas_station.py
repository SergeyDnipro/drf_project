import uuid
from django.db import models
from fuel_search.models.fuel import Fuel
from fuel_search.models.city import City


class GasStation(models.Model):

    station_number = models.SmallIntegerField(default=1, unique=True)
    station_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    location = models.ForeignKey(City, on_delete=models.CASCADE, null=False, related_name='location')
    fuel_type = models.ManyToManyField(Fuel, through='StationSupply')
    description = models.TextField(blank=True, null=True, max_length=300)

    def __str__(self):
        return f'{self.station_number} {self.station_id}'


class StationSupply(models.Model):
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE, related_name='station')
    location = models.ForeignKey(City, on_delete=models.CASCADE, null=False, related_name='location')
    fuel_t = models.ForeignKey(Fuel, on_delete=models.CASCADE, related_name='fuel_types')

    class Meta:
        unique_together = (('location', 'fuel_t', 'gas_station'),)
        ordering = ('location__city_name', 'gas_station__station_number')

    def __str__(self):
        return f' Номер заправки: {self.gas_station.station_number} - Вид топлива: {self.fuel_t.type_fuel}' \
               f' - Цена: {self.fuel_t.price} USD '

