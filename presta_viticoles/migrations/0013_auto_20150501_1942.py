# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0012_auto_20150501_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimate',
            name='description',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='name',
        ),
        migrations.AddField(
            model_name='estimate',
            name='company_name',
            field=models.CharField(null=True, max_length=45),
        ),
    ]
