from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    location = models.TextField()
    timestamp = models.DateTimeField(default = datetime.now)
    image = models.ImageField()



