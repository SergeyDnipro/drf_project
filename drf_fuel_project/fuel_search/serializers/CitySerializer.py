from rest_framework import views, serializers, generics
from fuel_search.models.fuel import Fuel
from fuel_search.models.city import City
from fuel_search.models.gas_station import GasStation, StationSupply


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StationSupply
        fields = (
            'gas_station',
            'fuel_t',
        )
        depth = 1




class CitySerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField(many=True)

    class Meta:
        model = City
        fields = (
            'city_name',
            'city_id',
            'location',
        )