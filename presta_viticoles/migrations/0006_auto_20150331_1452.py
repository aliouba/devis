# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0005_auto_20150320_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityprestaviticole',
            name='group',
            field=models.ForeignKey(related_query_name=b'activity', related_name='activities', to='presta_viticoles.ActivityGroup'),
            preserve_default=True,
        ),
    ]
