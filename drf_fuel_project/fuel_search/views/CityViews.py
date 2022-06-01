from rest_framework import viewsets
from fuel_search.serializers.CitySerializer import CitySerializer
from fuel_search.models.city import City


class CityView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    lookup_field = 'name__iexact'
    lookup_url_kwarg = 'name'

