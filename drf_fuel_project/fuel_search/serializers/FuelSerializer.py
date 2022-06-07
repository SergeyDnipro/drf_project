from rest_framework import serializers
from fuel_search.models.fuel import Fuel
from fuel_search.serializers.FuelStationSerializer import FuelStationSerializer


class FuelSerializer(serializers.ModelSerializer):
    fuel_on_station = FuelStationSerializer(many=True)

    class Meta:
        model = Fuel
        fields = (
            'id',
            'type',
            'fuel_on_station',
        )
