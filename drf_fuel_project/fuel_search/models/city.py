from django.db import models
from fuel_search.models.base_model import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, max_length=300)

    def __str__(self):
        return self.name
