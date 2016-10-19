from django.shortcuts import render
from rest_framework import viewsets
from .models import DiapositivaWeb
from .serializers import DiapositivaWebSerializer


class DiapositivaWebViewSet(viewsets.ModelViewSet):
    model            = DiapositivaWeb
    serializer_class = DiapositivaWebSerializer
    queryset         = DiapositivaWeb.objects.all()