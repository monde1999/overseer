from django.db import models
from django.contrib.auth.models import User

"""
report location
if location is not in proneAreas, then add
"""

class FloodProneArea(models.Model):
    locationX = models.FloatField
    locationY = models.FloatField
    water_volume = models.FloatField
    speed_to_subside = models.FloatField

class Weather(models.Model):
    temperature = models.FloatField
    rain = models.TextField

class FloodForecast(models.Model):
    location = FloodProneArea
    time = models.DateTimeField
    #weather = Weather

class Report(models.Model): #temp
    user = User
    location = FloodProneArea
    caption = models.TextField