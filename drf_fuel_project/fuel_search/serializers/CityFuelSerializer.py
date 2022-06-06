from rest_framework import serializers
from fuel_search.models.gas_station import Supply
from decimal import Decimal


class CityFuelSerializer(serializers.ModelSerializer):
    gas_station = serializers.CharField(source='gas_station.number')
    fuel = serializers.CharField(source='fuel.type')
    price_in_uah = serializers.SerializerMethodField()

    @staticmethod
    def get_price_in_uah(instance):
        return instance.price * Decimal(29.25)

    class Meta:
        model = Supply
        fields = (
            'id',
            'gas_station',
            'fuel',
            'price',
            'price_in_uah',
        )
