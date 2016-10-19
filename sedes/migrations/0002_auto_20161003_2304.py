# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 04:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sitios_web', '0001_initial'),
        ('sedes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zonas', '0002_auto_20161003_2304'),
        ('vias', '0002_auto_20161003_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='sede',
            name='sitio_web',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sitios_web.SitioWeb'),
        ),
        migrations.AddField(
            model_name='sede',
            name='ultimo_usuario_editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sedes_sede_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sede',
            name='usuario_creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sede',
            name='via',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vias.Via'),
        ),
        migrations.AddField(
            model_name='sede',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zonas.Zona'),
        ),
    ]
