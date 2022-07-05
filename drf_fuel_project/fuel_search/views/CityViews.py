from rest_framework import viewsets
from fuel_search.serializers.CitySerializer import CitySerializer
from fuel_search.models.city import City
from rest_framework.permissions import IsAuthenticated

class CityView(viewsets.ReadOnlyModelViewSet):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = CitySerializer
    queryset = City.objects.all()

    lookup_field = 'name__iexact'
    lookup_url_kwarg = 'name'
