from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Profession(models.Model):
    name = models.CharField(max_length=40, null=False)

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"

    def __str__(self):
        return self.name.capitalize()
    

class City(models.Model):
    name = models.CharField(max_length=40, null=False)
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name.capitalize()

         
class VehicleModel(models.Model):
    name = models.CharField(max_length=40, null=False)
    
    class Meta:
        verbose_name = "VehicleModel"
        verbose_name_plural = "VehicleModels"

    def __str__(self):
        return self.name.capitalize()

class Vehicle(models.Model):
    VEHICLES_TYPES = (
        ("camioneta","Camioneta"),
        ("motocicleta","Motocicleta"),
        ("automovil","Automovil")
    )
    type = models.CharField(choices=VEHICLES_TYPES, max_length=40, null=False)
    year = models.IntegerField(null=False)
    model = models.ForeignKey(VehicleModel, on_delete=DO_NOTHING)

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return "{} {} {}".format(self.type.capitalize(), self.model, self.year )           

class People(models.Model):
    GENDERS = (
        ("M","Masculino"),
        ("F","Femenino"),
    )
    cedula = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    dob = models.DateField(null=False) #Date of birth
    phone = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10,choices=GENDERS, default="M", null=False)
    address = models.CharField(max_length=150, null=False)
    profession = models.ForeignKey(Profession, on_delete=models.DO_NOTHING)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "People"
        verbose_name_plural = "People"

    def __str__(self):
        return "{} {}".format(self.fist_name.capitalize(), self.last_name.capitalize())        