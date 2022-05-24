import uuid
from django.db import models


class City(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city_name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, max_length=300)

    def __str__(self):
        return f'{self.city_name}'
