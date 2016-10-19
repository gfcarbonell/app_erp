# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='area_dependiente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='areas_areas_dependientes_related', to='areas.Area'),
        ),
    ]
