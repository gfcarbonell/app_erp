# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='observacion_dirección',
            new_name='observacion_direccion',
        ),
    ]
