# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 10:55
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'data source',
                'verbose_name_plural': 'data sources',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=16, verbose_name='identifier')),
                ('name_fi', models.CharField(blank=True, max_length=100, verbose_name='name in Finnish')),
                ('name_en', models.CharField(blank=True, max_length=100, verbose_name='name in English')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('coords', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='coordinates')),
                ('events', models.ManyToManyField(blank=True, related_name='locations', to='vehicles.EventType', verbose_name='events')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_timestamp', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='last timestamp')),
                ('origin_id', models.CharField(db_index=True, max_length=32, verbose_name='origin ID')),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicles', to='vehicles.DataSource')),
            ],
            options={
                'verbose_name': 'vehicle',
                'verbose_name_plural': 'vehicles',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations', to='vehicles.Vehicle', verbose_name='vehicle'),
        ),
        migrations.AlterUniqueTogether(
            name='vehicle',
            unique_together=set([('data_source', 'origin_id')]),
        ),
    ]
