# -*- encoding: utf-8 -*-
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import SliderWeb


class SliderWebSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SliderWeb
        fields = ['seccion_web', 'diapositiva_web', 'orden', 'activo']
