# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-06 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20170705_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indicadorred',
            options={'get_latest_by': 'fecha', 'verbose_name_plural': 'Indicadores'},
        ),
        migrations.AddField(
            model_name='indicatortype',
            name='tipo',
            field=models.CharField(default="RED", max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='IndicadorPAD',
        ),
        migrations.DeleteModel(
            name='IndicadorRedPAD',
        ),
    ]