# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-10-16 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0050_tasksconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorsValidationConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validate_urls', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Configuraciones de validaciones de indicadores',
            },
        ),
    ]