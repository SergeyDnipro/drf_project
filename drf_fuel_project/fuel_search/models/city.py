import uuid

from django.db import models


# Create your models here.
class City(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city_name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, max_length=300)
