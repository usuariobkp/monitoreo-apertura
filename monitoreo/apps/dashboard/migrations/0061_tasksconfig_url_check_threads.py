# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-11-28 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0060_auto_20191126_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksconfig',
            name='url_check_threads',
            field=models.IntegerField(default=1, verbose_name='Cantidad de threads a usar en el chequeo de links'),
        ),
    ]