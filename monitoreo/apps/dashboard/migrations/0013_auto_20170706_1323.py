# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-06 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20170706_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicatortype',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]