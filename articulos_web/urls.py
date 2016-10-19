# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^detalle/(?P<pk>\d+)/$$', views.ArticuloWebDetailView.as_view(), name='detalle'),
]