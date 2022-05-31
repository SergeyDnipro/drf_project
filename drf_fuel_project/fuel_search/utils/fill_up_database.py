from fuel_search.models.city import City
from fuel_search.models.fuel import Fuel
from fuel_search.models.gas_station import GasStation, Supply
import random


CITY_NAMES = ["Kyiv", "Kharkiv", "Lviv", "Odessa", "Dnipro"]


def fill_up_database_with_test_values():

    City.objects.bulk_create(
        [City(name=name, description={'description': f"Greate city of {name}"}) for name in CITY_NAMES],
        ignore_conflicts=True,
    )

    Fuel.objects.bulk_create(
        [Fuel(type=fuel_type) for fuel_type in Fuel.Type.All],
        ignore_conflicts=True
    )

    for city in City.objects.all():
        if GasStation.objects.filter(city=city).exists() is False:
            GasStation.objects.bulk_create(
                [GasStation(
                    number=random.randint(0, 32000),
                    city=city,
                    description=f'Gas Station in {city.name}',
                ) for _ in range(random.randint(1, 3))],
                ignore_conflicts=True,
            )

        for fuel in Fuel.objects.all():
            for station in GasStation.objects.filter(city=city):
                Supply.objects.get_or_create(
                    fuel=fuel,
                    gas_station=station,
                    defaults={
                        'price': 1 + random.random(),
                    }
                )

