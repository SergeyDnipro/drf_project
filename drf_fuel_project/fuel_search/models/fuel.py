from django.db import models
from fuel_search.models.base_model import BaseModel


class Fuel(BaseModel):
    class Type:
        a95 = 'A95'
        a92 = 'A92'
        dt = 'Diesel'
        lpg = 'LPG'
        All = (a95, a92, dt, lpg)
        All_django = [(x, x) for x in All]

    description = models.TextField(blank=True, null=True, max_length=300)

    type = models.CharField(
        max_length=20,
        choices=Type.All_django,
        unique=True,
    )

    def __str__(self):
        return self.type
