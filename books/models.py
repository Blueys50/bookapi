
from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    tag = models.CharField(max_length=50, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)


