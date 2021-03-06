# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 04:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0005_auto_20160905_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='nombre',
            field=models.CharField(db_index=True, help_text='Escribir el nombre de la entidad.', max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)]),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='numero_documento_identificacion',
            field=models.CharField(db_index=True, max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(20)], verbose_name='Número documento identificación'),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='siglas',
            field=models.CharField(db_index=True, max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
