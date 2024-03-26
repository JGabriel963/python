from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    min_age = models.PositiveIntegerField(default=12)
    activo = models.BooleanField(default=True)