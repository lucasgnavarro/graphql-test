from uuid import uuid4

from django.db import models
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return str(self.pk)
