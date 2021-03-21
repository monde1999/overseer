from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.utils import timezone

import requests
import json

from forecast.models import FloodForecast, Weather, FloodProneArea, Report
from forecast.serializers import FloodForecastSerializer, WeatherSerializer, FloodProneAreaSerializer, ReportSerializer

class FloodForecastViewSet(viewsets.ModelViewSet):
    queryset = FloodForecast.objects.all()
    serializer_class = FloodForecastSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        if (latitude is None or longitude is None):
            return self.queryset
        latitude = float(latitude)
        longitude = float(longitude)
        r = 5
        lat_min = latitude-r
        lat_max = latitude+r
        long_min = longitude-r
        long_max = longitude+r
        date_min = datetime.now() - timedelta(days=3)
        date_max = datetime.now() + timedelta(hours=1)
        queryset = self.queryset.filter(
            location__locationX__gte=lat_min, location__locationX__lte=lat_max,
            location__locationY__gte=long_min, location__locationY__lte=long_max,
            time__gte=date_min, time__lte=date_max)
        return queryset

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    # permission_classes = [permissions.IsAuthenticated]

class FloodProneAreaViewSet(viewsets.ModelViewSet):
    queryset = FloodProneArea.objects.all()
    serializer_class = FloodProneAreaSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        post_data = request.data
        print(post_data)
        #user = post_data['user']
        user = User.objects.get(pk=1)
        locX = post_data['locationX']
        locY = post_data['locationY']
        ts = post_data['timestamp']
        img = post_data['image']
        obj = Report(user=user, locationX=locX, locationY=locY,timestamp=ts,image=img)
        obj.save()
        q = FloodProneArea.objects.filter(locationX=locX,locationY=locY)
        if q.count()==0:
            fpa = FloodProneArea(locationX=locX, locationY=locY)
            fpa.save()

            url = 'http://api.openweathermap.org/data/2.5/weather'
            url += '?lat=' + locX + '&lon=' + locY
            url += '&appid=67aa636d02df1df62ef01de2db58fa49'
            r = requests.get(url)
            data = json.loads(r.content.decode())
            w_id = data['weather'][0]['id']
            w_temp = data['main']['temp']
            w_desc = data['weather'][0]['description']
            w_icon = data['weather'][0]['icon']
            w = Weather(w_id=w_id, w_temp=w_temp, w_description=w_desc, w_icon=w_icon)
            w.save()

            FloodForecast(location=fpa, weather=w).save()

        serializer_context = {
            'request': request,
        }
        return Response(ReportSerializer(obj, context=serializer_context).data)

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        if latitude is not None and longitude is not None:
            queryset = self.queryset.filter(locationX=latitude, locationY=longitude)
        else:
            queryset = self.queryset
        return queryset