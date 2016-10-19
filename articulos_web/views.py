from django.shortcuts import render
from django.views.generic import DetailView
from .models import ArticuloWeb

# Create your views here.
class ArticuloWebDetailView(DetailView):
    model = ArticuloWeb 
    template_name = 'articulo_web_create.html'


