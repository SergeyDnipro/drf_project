from rest_framework import serializers
from fuel_search.models.gas_station import Supply


class StationSupplySerializer(serializers.ModelSerializer):
    fuel = serializers.CharField(source='fuel.type')

    class Meta:
        model = Supply
        fields = (
            'gas_station',
            'fuel',
            'price',
        )
