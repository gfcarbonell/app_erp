# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-03 16:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('ultimo_nombre_host', models.CharField(max_length=255)),
                ('ultimo_direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('nombre', models.CharField(db_index=True, help_text='Escribir el nombre del área.', max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)])),
                ('siglas', models.CharField(db_index=True, max_length=10, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(10)])),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Correo electrónico (Institucional)')),
                ('fax_interno', models.CharField(blank=True, help_text='(Opcional).', max_length=20, null=True, verbose_name='Fax (Interno)')),
                ('anexo_interno', models.CharField(blank=True, help_text='(Opcional).', max_length=20, null=True, verbose_name='Anexo (Interno)')),
                ('mision', models.TextField(blank=True, help_text='(Opcional)', null=True, verbose_name='Misión')),
                ('vision', models.TextField(blank=True, help_text='(Opcional)', null=True, verbose_name='Visión')),
                ('logotipo', models.ImageField(blank=True, null=True, upload_to='logotipos_areas')),
                ('fecha_creacion', models.DateField(blank=True, null=True, verbose_name='Fecha creación')),
                ('fecha_cese', models.DateField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, help_text='(Opcional)', null=True, verbose_name='Descripción')),
                ('observacion', models.TextField(blank=True, help_text='(Opcional)', null=True, verbose_name='Observación')),
                ('activo', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('area_dependiente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='areas_areas_dependientes_related', to='areas.Area')),
            ],
            options={
                'verbose_name': 'Area',
                'db_table': 'Areas',
                'verbose_name_plural': 'Areas',
                'ordering': ('tipo_area', 'nombre'),
            },
        ),
    ]
