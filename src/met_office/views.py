from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from src.met_office.services.data_parser import DataParser
from src.met_office.services.met_office import Met_Office_Data
from .models import Regions, WeatherData,Parameters, ParametersValues
from .serializers import RegionsSerializer, WeatherSerializer
from pprint import pprint

class MetOfficeViewSet():

    @swagger_auto_schema(methods=['GET'])
    @api_view(['GET'])
    def get_records(request):
        region_id = 1
        dp = DataParser()
        gd = Met_Office_Data()

        text_data = gd.get_data()

        data = dp.parseData(text_data)
        reg = Regions.objects.all().first()
        pra = Parameters.objects.all().first()
        for dt in data:
            for month in dt.keys():
                months_data = dt[month];
                for year in months_data.keys():
                    value = months_data[year]
                    if year == '---':
                        continue
                    w = WeatherData(year=year, month_season=month, region_id=reg)
                    w.save();
                    if value == ' ---':
                        continue
                    p = ParametersValues(parameter_id=pra,weather_id= w, value=value )
                    p.save();

        return Response({"data":data},status=200)


    
    @swagger_auto_schema(methods=['post'], request_body=RegionsSerializer,responses={200: RegionsSerializer})
    @api_view(['POST'])
    def save_records(request):
        serializer = RegionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status=401)    
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)   
          
    
    @swagger_auto_schema(methods=['GET'])
    @api_view(['GET'])
    def get_records_from_db(request, region_id, parameter_id):
        print("region_id",region_id)
        print("parameter_id",parameter_id)

        parameter_values = ParametersValues.objects.filter(parameter_id=parameter_id).filter(weather_id__region_id=region_id).all()
        
        return Response(list(parameter_values.values()),status=200)


     
    