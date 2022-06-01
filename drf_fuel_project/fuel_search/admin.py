from django.contrib import admin
from .models.city import City
from .models.fuel import Fuel
from .models.gas_station import GasStation, Supply

admin.site.register(City)
admin.site.register(Fuel)
admin.site.register(GasStation)
admin.site.register(Supply)

# Register your models here.
