from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip(models.Model):
    location = models.CharField(max_length=100)
    trip_length = models.IntegerField(blank=True)
    date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")

    def __str__(self):
        return self.location