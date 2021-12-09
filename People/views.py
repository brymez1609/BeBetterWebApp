from django.shortcuts import render
from People.models import City, People, Profession, Vehicle, VehicleModel
from People.serializers import CitySerializer, PeopleSerializer, ProfessionSerializer, VehicleModelSerializer, VehicleSerializer
from People.models import People as PeopleModel
from rest_framework import viewsets
# Create your views here.
class PeopleViewSet(viewsets.ModelViewSet):
    queryset = PeopleModel.objects.all()
    serializer_class = PeopleSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer 


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer 

class VehicleModelViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer 


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer 