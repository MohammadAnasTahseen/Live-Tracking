from django.db import models

# Create your models here.

class DiverLocationUpdate(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
 
    timestamp = models.DateTimeField(auto_now_add=True)
