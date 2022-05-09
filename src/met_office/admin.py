
# Register your models here.
from django.contrib import admin
from .models import Regions, WeatherData,Parameters, ParametersValues


# Register your models here.
@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = ['regionID', 'region', 'country']


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['weatherdataID', 'year', 'month_season','created_at','region_id']