import uuid
from django.db import models


class GasStation(models.Model):
    station_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=50)
    description = models.TextField(null=True, max_length=300)
    url = models.URLField(max_length=200)
