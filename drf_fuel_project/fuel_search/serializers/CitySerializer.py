from rest_framework import serializers
from fuel_search.models.city import City
from fuel_search.serializers.GasStationSerializer import GasStationSerializer


class CitySerializer(serializers.ModelSerializer):
    stations = GasStationSerializer(many=True)

    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'stations',
        )
