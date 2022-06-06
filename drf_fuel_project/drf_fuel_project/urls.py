from django.contrib import admin
from django.urls import path
from fuel_search.views.CityViews import CityView
from fuel_search.views.FuelViews import FuelView
from fuel_search.views.CityFuelView import CityFuelView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('city/<str:name>/', CityView.as_view({'get': 'retrieve'})),
    path('cities/', CityView.as_view({'get': 'list'})),
    path('fuel/<str:type>/', FuelView.as_view({'get': 'retrieve'})),
    path('city&fuel/', CityFuelView.as_view({'get': 'list'})),
]
