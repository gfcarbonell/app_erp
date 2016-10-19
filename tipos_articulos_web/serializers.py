# -*- encoding: utf-8 -*-
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import TipoArticuloWeb


class TipoArticuloWebSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoArticuloWeb
        fields = ['nombre']
