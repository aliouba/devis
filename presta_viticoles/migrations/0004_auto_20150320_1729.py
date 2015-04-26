# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0003_auto_20150320_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefit',
            name='creationdate',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='distance_entre_ceps',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='estimate',
            field=models.ForeignKey(to='presta_viticoles.Estimate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='largeur_entre_rangs',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='modificationdate',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='nb',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='price_with_tax',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='price_without_tax',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='surface',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='surface_manquant',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='tax',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='unit_price',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='benefit',
            name='unit_type',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estimate',
            name='customer',
            field=models.ForeignKey(related_query_name=b'estimate', related_name='estimates', to='presta_viticoles.Customer'),
            preserve_default=True,
        ),
    ]
