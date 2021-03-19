from rest_framework import serializers
from forecast.models import FloodForecast, Weather, FloodProneArea, Report
from django.contrib.auth.models import User

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Report
        fields = '__all__'

class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class FloodProneAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FloodProneArea
        fields = '__all__'

class FloodForecastSerializer(serializers.HyperlinkedModelSerializer):
    location = FloodProneAreaSerializer()
    weather = WeatherSerializer()
    class Meta:
        model = FloodForecast
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username',]