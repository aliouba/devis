# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0006_auto_20150331_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benefit',
            name='distance_entre_ceps',
        ),
        migrations.RemoveField(
            model_name='benefit',
            name='largeur_entre_rangs',
        ),
        migrations.RemoveField(
            model_name='benefit',
            name='nb',
        ),
        migrations.RemoveField(
            model_name='benefit',
            name='surface',
        ),
        migrations.RemoveField(
            model_name='benefit',
            name='surface_manquant',
        ),
        migrations.RemoveField(
            model_name='configprestaviticole',
            name='cepage',
        ),
        migrations.RemoveField(
            model_name='configprestaviticole',
            name='deplacement',
        ),
        migrations.RemoveField(
            model_name='configprestaviticole',
            name='pente',
        ),
        migrations.RemoveField(
            model_name='configprestaviticole',
            name='plant_manquant',
        ),
        migrations.AddField(
            model_name='activityprestaviticole',
            name='tax',
            field=models.DecimalField(default=0, null=True, max_digits=10, decimal_places=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configprestaviticole',
            name='nb_plants_min',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimate',
            name='distance_entre_ceps',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimate',
            name='largeur_entre_rangs',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimate',
            name='nb',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimate',
            name='plant_superficie',
            field=models.CharField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimate',
            name='price_with_tax',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimate',
            name='price_without_tax',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimate',
            name='surface',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimate',
            name='type_guyot',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
