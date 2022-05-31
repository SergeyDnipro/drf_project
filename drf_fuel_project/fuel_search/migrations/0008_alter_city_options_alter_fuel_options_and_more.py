# Generated by Django 4.0.4 on 2022-05-31 16:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_search', '0007_alter_gasstation_fuel_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='fuel',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='gasstation',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='stationsupply',
            options={'ordering': ('gas_station__number',)},
        ),
        migrations.RenameField(
            model_name='city',
            old_name='city_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='fuel',
            old_name='type_fuel',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='gasstation',
            old_name='fuel_type',
            new_name='fuel_types',
        ),
        migrations.AlterUniqueTogether(
            name='stationsupply',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='city',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='price',
        ),
        migrations.RemoveField(
            model_name='gasstation',
            name='station_id',
        ),
        migrations.RemoveField(
            model_name='gasstation',
            name='station_number',
        ),
        migrations.AddField(
            model_name='city',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='city',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='fuel',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='gasstation',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='gasstation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='gasstation',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fuel_search.city'),
        ),
        migrations.AddField(
            model_name='gasstation',
            name='number',
            field=models.SmallIntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name='stationsupply',
            old_name='fuel_t',
            new_name='fuel',
        ),
        migrations.AddField(
            model_name='stationsupply',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='In USD', max_digits=9),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stationsupply',
            name='gas_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fuel_search.gasstation'),
        ),
        migrations.AlterUniqueTogether(
            name='stationsupply',
            unique_together={('fuel', 'gas_station')},
        ),
        migrations.RemoveField(
            model_name='stationsupply',
            name='location',
        ),
    ]