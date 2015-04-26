# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityPrestaViticole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('price_plant_gd', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('price_plant_gs', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('price_ha_gs', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('price_ha_gd', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nb', models.FloatField(null=True)),
                ('largeur_entre_rangs', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('distance_entre_ceps', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('surface', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('surface_manquant', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('unit_price', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('unit_type', models.CharField(max_length=45)),
                ('price_with_tax', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('price_without_tax', models.DecimalField(null=True, max_digits=10, decimal_places=0)),
                ('tax', models.DecimalField(null=True, max_digits=10, decimal_places=0)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('activity', models.ForeignKey(to='presta_viticoles.ActivityPrestaViticole')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('siret', models.CharField(max_length=14, null=True, blank=True)),
                ('phonenumber', models.CharField(max_length=45, null=True, blank=True)),
                ('mail', models.CharField(max_length=45, null=True, blank=True)),
                ('cp', models.CharField(max_length=45, null=True, blank=True)),
                ('city', models.CharField(max_length=45, null=True, blank=True)),
                ('adresse', models.CharField(max_length=45, null=True, blank=True)),
                ('country', models.CharField(max_length=45, null=True, blank=True)),
                ('logo', models.FileField(max_length=45, null=True, upload_to=b'', blank=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfigPrestaViticole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guyots', models.BooleanField(default=False)),
                ('guyotd', models.BooleanField(default=False)),
                ('superficie', models.BooleanField(default=False)),
                ('plant', models.BooleanField(default=False)),
                ('plant_manquant', models.BooleanField(default=False)),
                ('deplacement', models.BooleanField(default=False)),
                ('pente', models.BooleanField(default=False)),
                ('cepage', models.BooleanField(default=False)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('company', models.ForeignKey(to='presta_viticoles.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=45, null=True)),
                ('lastname', models.CharField(max_length=45, null=True)),
                ('phonenumber', models.CharField(max_length=45, null=True)),
                ('mail', models.CharField(max_length=45, null=True)),
                ('cp', models.CharField(max_length=45, null=True)),
                ('city', models.CharField(max_length=45, null=True)),
                ('adresse', models.CharField(max_length=45, null=True)),
                ('country', models.CharField(max_length=45, null=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=45, null=True)),
                ('lastname', models.CharField(max_length=45, null=True)),
                ('phonenumber', models.CharField(max_length=45, null=True)),
                ('mail', models.CharField(max_length=45, null=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('company', models.ForeignKey(to='presta_viticoles.Company')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('customer', models.ForeignKey(to='presta_viticoles.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='benefit',
            name='estimate',
            field=models.ForeignKey(to='presta_viticoles.Estimate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activityprestaviticole',
            name='company',
            field=models.ForeignKey(to='presta_viticoles.Company'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activityprestaviticole',
            name='group',
            field=models.ForeignKey(related_query_name=b'group', related_name='groups', to='presta_viticoles.ActivityGroup'),
            preserve_default=True,
        ),
    ]
