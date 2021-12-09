from rest_framework import  serializers
from .models import *
# Serializers define the API representation.



class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'                                

class VehicleSerializer(serializers.ModelSerializer):
    model = VehicleModelSerializer()
    class Meta:
        model = Vehicle
        fields = '__all__'                     
        

class PeopleSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    vehicle = VehicleSerializer()
    profession = ProfessionSerializer()
    class Meta:
        model = People
        fields = '__all__'        