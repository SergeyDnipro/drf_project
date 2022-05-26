from rest_framework import generics
from fuel_search.serializers.CitySerializer import *
from fuel_search.models.city import City
from fuel_search.models.fuel import Fuel
from fuel_search.models.gas_station import GasStation, StationSupply

class CitySerializerView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self, **kwargs):
        key = list(self.kwargs.keys())[0]
        key_val = self.kwargs[key]
        return City.objects.filter(**{key: key_val})
