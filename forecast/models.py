from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

"""
report location
if location is not in proneAreas, then add
"""

class FloodProneArea(models.Model):
    locationX = models.FloatField()
    locationY = models.FloatField()
    water_volume = models.FloatField(default=0)
    speed_to_subside = models.FloatField(default=0)

    def __str__(self):
        return str(self.locationX) + ", " +str (self.locationY)

class Weather(models.Model):
    w_id = models.IntegerField(default=0)
    w_temp = models.FloatField(default=0)

    def __str__(self):
        return str(self.w_id) + ", " + str(self.w_temp)

class FloodForecast(models.Model):
    location = models.ForeignKey(FloodProneArea, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default = datetime.now)
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.location)

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    locationX = models.FloatField()
    locationY = models.FloatField()
    timestamp = models.DateTimeField(default = datetime.now)
    image = models.ImageField(blank=True)

    def __str__(self):
        return str(self.locationX) + ", " + str(self.locationY)