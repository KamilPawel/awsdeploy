from django.db import models
from django.utils import timezone


class Time(models.Model):
    code = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
