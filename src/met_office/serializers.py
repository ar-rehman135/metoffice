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



