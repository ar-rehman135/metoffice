from tkinter.tix import Tree
import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _
from src.services.banxico import BanxicoService
from src.users.models import User


class Regions(models.Model):
    
    regionID = models.AutoField(primary_key=True)
    region = models.CharField(max_length = 100,unique=True)
    country = models.CharField(max_length = 100, unique=True)
    
    def __str__(self):
        return str(self.regionID) + " : " + str(self.region) + " : " + str (self.country)



class WeatherData(models.Model):
    weatherdataID = models.AutoField(primary_key=True)
    year = models.IntegerField(max_length=100)
    month_season = models.CharField(max_length=250)
    created_at= models.DateTimeField(auto_now_add=True)
    region_id = models.ForeignKey(Regions,on_delete=models.DO_NOTHING,blank=True, null=True)
    class Meta:
        unique_together = ('year', 'month_season','region_id')

    # def __str__(self):
    #     return str(self.weatherdataID) + " : " + int(self.year) + " : " + str (self.month_season)
    

class Parameters(models.Model):
    
    parameterID = models.AutoField(primary_key=True)
    parameter_name = models.CharField(max_length = 100,unique=True)


class ParametersValues(models.Model):
    parametervalueID = models.AutoField(primary_key=True)
    parameter_id = models.ForeignKey(Parameters,on_delete=models.DO_NOTHING, blank=True, null=True)
    weather_id = models.ForeignKey(WeatherData,on_delete=models.DO_NOTHING, blank=True, null=True, related_name="weather")
    value = models.FloatField()

    class Meta:
        unique_together = ('parameter_id', 'weather_id')
    



