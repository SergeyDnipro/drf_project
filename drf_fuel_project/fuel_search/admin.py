from django.contrib import admin
from .models.city import City
from .models.fuel import Fuel
from .models.gas_station import GasStation, StationSupply

admin.site.register(City)
admin.site.register(Fuel)
admin.site.register(GasStation)
admin.site.register(StationSupply)

# Register your models here.
