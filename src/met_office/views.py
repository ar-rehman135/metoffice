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

class MetOfficeViewSet():

    @swagger_auto_schema(methods=['GET'])
    @api_view(['GET'])
    def get_records(request):
        dp = DataParser()
        gd = Met_Office_Data()

        text_data = gd.get_data()

        data = dp.parseData(text_data)
        return Response({"data":data},status=200)

    
    
    