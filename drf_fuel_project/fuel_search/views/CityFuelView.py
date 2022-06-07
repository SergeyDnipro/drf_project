from rest_framework import viewsets
from fuel_search.serializers.CityFuelSerializer import CityFuelSerializer
from fuel_search.models.gas_station import GasStation, Supply
from django.db.models import Q

# Отображение обектов, содержащихся в запросе с ключами "city" и "type"
class CityFuelView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CityFuelSerializer

    def get_queryset(self):
        city = self.request.GET.get('city')
        type = self.request.GET.get('type')
        return Supply.objects.filter(Q(gas_station__city__name=city) & Q(fuel__type=type))
