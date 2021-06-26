from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    description = models.TextField(null=True,blank=True)
    floodLevel = models.IntegerField()
    # location = models.TextField()
    locationX = models.FloatField()
    locationY = models.FloatField()
    timestamp = models.DateTimeField(default = datetime.now)
    image = models.ImageField(null = True, blank = True)

    class Meta:
        db_table='report'

