# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0008_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mail',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
