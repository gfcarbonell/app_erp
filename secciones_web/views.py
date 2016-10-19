from django.shortcuts import render
from rest_framework import viewsets
from .models import SeccionWeb
from .serializers import SeccionWebSerializer


class SeccionWebViewSet(viewsets.ModelViewSet):
    model            = SeccionWeb
    serializer_class = SeccionWebSerializer
    queryset         = SeccionWeb.objects.all()