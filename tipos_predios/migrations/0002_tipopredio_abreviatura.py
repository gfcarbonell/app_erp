# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-05 18:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipos_predios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipopredio',
            name='abreviatura',
            field=models.CharField(db_index=True, default='', max_length=10, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(10)]),
            preserve_default=False,
        ),
    ]