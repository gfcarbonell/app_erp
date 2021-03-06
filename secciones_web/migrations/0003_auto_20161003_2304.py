# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 04:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipos_secciones_web', '0002_auto_20161003_2304'),
        ('secciones_web', '0002_seccionweb_sitio_web'),
        ('diapositivas_web', '0004_auto_20160909_2054'),
        ('sliders_web', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='seccionweb',
            name='sliders_web',
            field=models.ManyToManyField(through='sliders_web.SliderWeb', to='diapositivas_web.DiapositivaWeb'),
        ),
        migrations.AddField(
            model_name='seccionweb',
            name='tipo_seccion_web',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipos_secciones_web.TipoSeccionWeb'),
        ),
        migrations.AddField(
            model_name='seccionweb',
            name='ultimo_usuario_editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secciones_web_seccionweb_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seccionweb',
            name='usuario_creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
