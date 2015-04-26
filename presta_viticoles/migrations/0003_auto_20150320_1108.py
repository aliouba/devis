# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0002_auto_20150320_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='adresse',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='cp',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='firstname',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastname',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='mail',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
    ]
