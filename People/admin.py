from django.contrib import admin

from People.models import *

# Register your models here.

admin.site.register(People)
admin.site.register(City)
admin.site.register(Profession)
admin.site.register(VehicleModel)    
admin.site.register(Vehicle)