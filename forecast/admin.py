from django.contrib import admin
from forecast.models import FloodProneArea, Weather, FloodForecast, Report

admin.site.register(FloodProneArea)
admin.site.register(Weather)
admin.site.register(FloodForecast)
admin.site.register(Report)