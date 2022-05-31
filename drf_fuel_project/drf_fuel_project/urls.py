from django.contrib import admin
from django.urls import path
from fuel_search.views.CityViews import CityView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('city/<str:name>/', CityView.as_view({'get': 'retrieve'})),
    path('cities/', CityView.as_view({'get': 'list'})),
#   path('station/<str:station_number>', GasStationNumberSerializerView.as_view())
]
