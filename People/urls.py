from django.urls import include,path
from People.views import CityViewSet, PeopleViewSet, ProfessionViewSet, VehicleViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'people', PeopleViewSet)
city_list = CityViewSet.as_view({
    'get': 'list',
})
vehicle_list = VehicleViewSet.as_view({
    'get': 'list',
})
profession_list = ProfessionViewSet.as_view({
    'get': 'list',
})
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('city/', city_list, name='city-list'),
    path('vehicle/', vehicle_list, name='vehicle-list'),
    path('profession/', profession_list, name='profession-list'),
]
