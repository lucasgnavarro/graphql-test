from django.db import models

from apps.core.models import BaseModel


class Student(BaseModel):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.TextField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
