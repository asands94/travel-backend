from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PRIORITIES = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low')
)

class Itinerary(models.Model):
    location = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITIES,
        default=PRIORITIES[0][0]
    )

    def __str__(self):
        return self.location

class Trip(models.Model):
    location = models.CharField(max_length=100)
    trip_length = models.IntegerField(blank=True)
    date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    itineraries = models.ManyToManyField(Itinerary)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")

    def __str__(self):
        return self.location