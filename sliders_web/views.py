from django.shortcuts import render
from rest_framework import viewsets
from .models import SliderWeb
from .serializers import SliderWebSerializer


class SliderWebViewSet(viewsets.ModelViewSet):
    model            = SliderWeb
    serializer_class = SliderWebSerializer
    queryset         = SliderWeb.objects.all()