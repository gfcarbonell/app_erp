from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoSeccionWeb
from .serializers import TipoSeccionWebSerializer


class TipoSeccionWebViewSet(viewsets.ModelViewSet):
    model            = TipoSeccionWeb
    serializer_class = TipoSeccionWebSerializer
    queryset         = TipoSeccionWeb.objects.all()