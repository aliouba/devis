# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefit',
            name='estimate',
            field=models.ForeignKey(related_query_name=b'estimate', related_name='estimates', to='presta_viticoles.Estimate'),
            preserve_default=True,
        ),
    ]
