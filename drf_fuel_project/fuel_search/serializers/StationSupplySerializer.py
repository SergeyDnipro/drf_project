from rest_framework import serializers
from fuel_search.models.gas_station import Supply
from decimal import Decimal


class StationSupplySerializer(serializers.ModelSerializer):
    fuel = serializers.CharField(source='fuel.type')

    price_in_uah = serializers.SerializerMethodField()

    def get_price_in_uah(self, instance):
        return instance.price * Decimal(29.25)

    class Meta:
        model = Supply
        fields = (
            'gas_station',
            'fuel',
            'price',
            'price_in_uah',
        )
