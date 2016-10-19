# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20161005_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='observacion',
        ),
        migrations.AddField(
            model_name='empleado',
            name='descripcion_empleado',
            field=models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Descripción (Empleado)'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='observacion_empleado',
            field=models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Observación (Empleado)'),
        ),
    ]
