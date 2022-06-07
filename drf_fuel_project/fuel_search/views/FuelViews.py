from rest_framework import viewsets
from fuel_search.serializers.FuelSerializer import FuelSerializer
from fuel_search.models.fuel import Fuel


class FuelView(viewsets.ReadOnlyModelViewSet):
    serializer_class = FuelSerializer
    queryset = Fuel.objects.all()

    lookup_field = 'type__iexact'
    lookup_url_kwarg = 'type'
