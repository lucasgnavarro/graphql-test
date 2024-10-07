from django.db import models


class AdmissionProcess(models.Model):
    APPLICATION_TARGET_TYPE_CHOICES = [
        ('SCHOOL', 'School'),
        ('PROGRAM', 'Program'),
    ]

    id = models.CharField(max_length=80, primary_key=True)  # Datatype is not ideal, but i've got this on schema definition
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    short_name_admin = models.CharField(max_length=255)
    short_name_display = models.CharField(max_length=255)
    application_target_type = models.CharField(max_length=10, choices=APPLICATION_TARGET_TYPE_CHOICES)
    display_in_public_school_directory = models.BooleanField(default=True)

    def __str__(self):
        return self.name
