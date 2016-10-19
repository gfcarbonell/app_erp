# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('secciones_web', '0001_initial'),
        ('sitios_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccionweb',
            name='sitio_web',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitios_web.SitioWeb'),
        ),
    ]
