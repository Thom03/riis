# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 12:58
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_highway'),
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4210)),
            ],
            options={
                'verbose_name': 'Houses',
            },
        ),
    ]
