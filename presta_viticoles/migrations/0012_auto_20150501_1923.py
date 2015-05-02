# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0011_auto_20150418_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefit',
            name='description',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='benefit',
            name='name',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='estimate',
            name='description',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='estimate',
            name='name',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
