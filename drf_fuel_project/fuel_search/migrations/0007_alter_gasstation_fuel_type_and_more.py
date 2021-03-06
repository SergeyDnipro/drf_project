# Generated by Django 4.0.4 on 2022-05-22 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_search', '0006_alter_stationsupply_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasstation',
            name='fuel_type',
            field=models.ManyToManyField(through='fuel_search.StationSupply', to='fuel_search.fuel'),
        ),
        migrations.AlterField(
            model_name='stationsupply',
            name='fuel_t',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuel_types', to='fuel_search.fuel'),
        ),
    ]
