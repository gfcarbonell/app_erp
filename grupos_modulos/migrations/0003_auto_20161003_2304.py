# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 04:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos_modulos', '0002_auto_20160901_2344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupomodulo',
            options={'ordering': ('nombre',), 'verbose_name': 'Grupo Módulo', 'verbose_name_plural': 'Grupos Módulos'},
        ),
        migrations.AlterField(
            model_name='grupomodulo',
            name='nombre',
            field=models.CharField(db_index=True, help_text='Escribir el nombre del grupo módulo.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)]),
        ),
    ]
