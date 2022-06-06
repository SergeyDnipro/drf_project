from django.db import models
from fuel_search.models.fuel import Fuel
from fuel_search.models.city import City
from fuel_search.models.base_model import BaseModel


class GasStation(BaseModel):
    number = models.SmallIntegerField(unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, related_name='stations')
    fuels = models.ManyToManyField(Fuel, through='Supply', related_name='fuel_types')
    description = models.TextField(blank=True, null=True, max_length=300)

    def __str__(self):
        return f'{self.number} {self.id}'


class Supply(models.Model):
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE, related_name='supplies')
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, related_name='fuel_on_station')
    price = models.DecimalField(default=0.0, max_digits=9, decimal_places=2, help_text="In USD")

    class Meta:
        unique_together = (('fuel', 'gas_station'), )
        ordering = ('gas_station__number', )

    def __str__(self):
        return f' Номер заправки: {self.gas_station.number} - Вид топлива: {self.fuel.type}' \
               f' - Цена: {self.price} USD'
