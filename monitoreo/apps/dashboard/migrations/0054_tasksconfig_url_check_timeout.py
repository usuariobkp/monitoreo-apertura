# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-29 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0053_merge_20191029_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksconfig',
            name='url_check_timeout',
            field=models.IntegerField(default=1, help_text='En segundos.'),
        ),
    ]
