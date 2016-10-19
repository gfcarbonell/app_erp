# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 04:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('redes_sociales', '0003_redsocial_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoSitioWebRedSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('ultimo_nombre_host', models.CharField(max_length=255)),
                ('ultimo_direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('orden', models.SmallIntegerField(unique=True)),
                ('url', models.URLField(db_index=True, unique=True)),
                ('descripcion', models.TextField(blank=True, help_text='(Opcional)', null=True)),
                ('observacion', models.TextField(blank=True, help_text='(Opcional)', null=True)),
                ('activo', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('red_social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redes_sociales.RedSocial')),
            ],
            options={
                'db_table': 'Catalogos_Sitios_Web_Redes_Sociales',
                'verbose_name': 'Catalogo Sitio Web Red Social',
                'ordering': ('orden',),
                'verbose_name_plural': 'Catalogos Sitios Web Redes Sociales',
            },
        ),
    ]
