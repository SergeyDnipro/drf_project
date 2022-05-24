import uuid
from django.db import models


class Fuel(models.Model):

    class TypeFuel():
        a95 = 'A95'
        a92 = 'A92'
        dt = 'Diesel'
        lpg = 'LPG'
        All = (a95, a92, dt, lpg)
        All_django = ((x, x) for x in All)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True, max_length=300)

    type_fuel = models.CharField(
        max_length=20,
        choices=TypeFuel.All_django,
        unique=True,
    )


    def __str__(self):
        return f'{self.type_fuel} {self.price}'

