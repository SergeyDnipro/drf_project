# Generated by Django 4.0.4 on 2022-05-22 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_search', '0005_alter_stationsupply_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stationsupply',
            options={'ordering': ('location__city_name', 'gas_station__station_number')},
        ),
    ]
