from django.db import models

# Create your models here.
from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name