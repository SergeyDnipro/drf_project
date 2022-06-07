from rest_framework import serializers
from fuel_search.models.gas_station import Supply, GasStation
from decimal import Decimal


class FuelStationSerializer(serializers.ModelSerializer):
    gas_station = serializers.CharField(source='gas_station.number')
    city = serializers.CharField(source='gas_station.description')
    price_in_uah = serializers.SerializerMethodField()

    @staticmethod
    def get_price_in_uah(instance):
        return instance.price * Decimal(29.25)

    class Meta:
        model = Supply
        fields = (
            'gas_station',
            'city',
            'price',
            'price_in_uah',
        )
