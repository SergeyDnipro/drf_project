import uuid
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ('-created', )

    created = models.DateTimeField(default=timezone.now, db_index=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
