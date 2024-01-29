from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Province, Regency, District, SubDistrict, Village
from .serializers import ProvinceSerializer, RegencySerializer, DistrictSerializer, SubDistrictSerializer, VillageSerializer
from .renderer import CustomRenderer
import requests

class ProvinceView(APIView):
    renderer_classes = [CustomRenderer]

    def get(self, request, *args, **kwargs):
        provinces = Province.objects.all()
        serializer = ProvinceSerializer(provinces, many=True)
        provinces = requests.get('https://emsifa.github.io/api-wilayah-indonesia/api/provinces.json')
        for data in provinces.json():
            province = Province.objects.create(name=data['name'])
            regencies = requests.get('https://emsifa.github.io/api-wilayah-indonesia/api/regencies/' + str(data['id']) + '.json')
            for data in regencies.json():
                regency = Regency.objects.create(name=data['name'], province_id=province.id)
                districts = requests.get('https://emsifa.github.io/api-wilayah-indonesia/api/districts/' + str(data['id']) + '.json')
                for data in districts.json():
                    district = District.objects.create(name=data['name'], regency_id=regency.id)
                    subdistricts = requests.get('https://emsifa.github.io/api-wilayah-indonesia/api/villages/' + str(data['id']) + '.json')
                    for data in subdistricts.json():
                        SubDistrict.objects.create(name=data['name'], district_id=district.id)
                        
        return Response(serializer.data)