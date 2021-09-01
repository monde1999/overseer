from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    description = models.TextField(null=True,blank=True)
    floodLevel = models.IntegerField()
    locationX = models.FloatField()
    locationY = models.FloatField()
    timestamp = models.DateTimeField(default = datetime.now)

    class Meta:
        db_table='report'

class Report_Images(models.Model):
    image = models.ImageField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    class Meta:
        db_table = 'report_images'