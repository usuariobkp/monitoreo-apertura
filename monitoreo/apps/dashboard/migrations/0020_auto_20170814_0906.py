# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20170803_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicadorred',
            name='indicador_valor',
            field=models.TextField(),
        ),
    ]
