from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField(default=12)
    active = models.BooleanField(default=True)
 

 