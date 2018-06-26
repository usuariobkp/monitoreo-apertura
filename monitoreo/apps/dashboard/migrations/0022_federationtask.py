# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_harvestingnode'),
    ]

    operations = [
        migrations.CreateModel(
            name='FederationTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('RUNNING', 'Procesando cat\xe1logos'), ('FINISHED', 'Finalizada')], max_length=20)),
                ('created', models.DateTimeField()),
                ('finished', models.DateTimeField(null=True)),
                ('logs', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Corridas de Federaci\xf3n',
            },
        ),
    ]