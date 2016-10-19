# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^empleado/nuevo/$', views.EmpleadoCreateView.as_view(), name='create'),
    url(r'^empleados/$', views.EmpleadoControlListView.as_view(), name='list'),
]