from rest_framework import serializers



from rest_framework import serializers
from .models import Regions, WeatherData,Parameters, ParametersValues

class RegionsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Regions
        fields = "__all__"


class WeatherSerializer(serializers.ModelSerializer):


    class Meta:
        model = WeatherData
        fields = "__all__"


class WeatherDataSerializer(serializers.ModelSerializer):


    class Meta:
        model = WeatherData
        fields = ['year', 'month_season']

class ParametersValuesSerializer(serializers.ModelSerializer):
   
    weather_id = WeatherDataSerializer(required=True)
    class Meta:
        model = ParametersValues
        fields = "__all__"
        



   

