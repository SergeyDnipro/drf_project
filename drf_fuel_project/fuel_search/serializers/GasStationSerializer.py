from fuel_search.models.gas_station import GasStation
from fuel_search.serializers.StationSupplySerializer import StationSupplySerializer
from rest_framework import serializers


class GasStationSerializer(serializers.ModelSerializer):
    supplies = StationSupplySerializer(many=True)

    class Meta:
        model = GasStation
        fields = (
            'id',
            'supplies',
            'city',
            'description',
        )
