# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0010_auto_20150407_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityprestaviticole',
            name='group',
            field=models.ForeignKey(related_query_name='activity', to='presta_viticoles.ActivityGroup', related_name='activities'),
        ),
        migrations.AlterField(
            model_name='benefit',
            name='estimate',
            field=models.ForeignKey(related_query_name='estimate', to='presta_viticoles.Estimate', related_name='estimates'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(upload_to='', max_length=45, null=True, blank=True),
        ),
    ]
