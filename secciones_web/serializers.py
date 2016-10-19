# -*- encoding: utf-8 -*-
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import SeccionWeb


class SeccionWebSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeccionWeb
        fields = [
        			'sitio_web', 'tipo_seccion_web', 'catalogo_menu_sub_menu', 'sliders_web',
        			'nombre', 'banner', 'descripcion', 'observacion',
        		 ]
