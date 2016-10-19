from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoArticuloWeb
from .serializers import TipoArticuloWebSerializer


class TipoArticuloWebViewSet(viewsets.ModelViewSet):
    model            = TipoArticuloWeb
    serializer_class = TipoArticuloWebSerializer
    queryset         = TipoArticuloWeb.objects.all()