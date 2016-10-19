# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-19 00:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import personas.validators


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_auto_20161008_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='denominacion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Denominación'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fotografia',
            field=models.ImageField(blank=True, help_text='Subir fotografia (Opcional).', null=True, upload_to='fotografia_persona', validators=[personas.validators.valid_extension], verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='numero_hijo',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='Escribir número(s) de hijo(s).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Número de hijo(s)'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='pabellon',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Pabellón'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='zona_secccion',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Zona (Sección)'),
        ),
    ]