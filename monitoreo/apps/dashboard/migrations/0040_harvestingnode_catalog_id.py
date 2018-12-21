# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-14 13:02
from __future__ import unicode_literals

from django.db import migrations, models


def set_catalog_id(apps, _schema_editor):
    HarvestingNode = apps.get_model("dashboard", "HarvestingNode")
    nodes = HarvestingNode.objects.all()
    for node in nodes:
        node.catalog_id = node.name
        node.save()


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_indicatortype_series_indexadores'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvestingnode',
            name='catalog_id',
            field=models.CharField(null=True, max_length=100)
        ),
        migrations.RunPython(set_catalog_id, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='harvestingnode',
            name='catalog_id',
            field=models.CharField(max_length=100, unique=True)
        )
    ]