# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^modulos/$', views.CatalagoModuloMenuTemplateView.as_view(), name='main'),
    url(r'^tramite-documentario/$', views.TramiteDocumentarioTemplateView.as_view(), name='tramite_documentario'),
    url(r'^tramite-documentario/menu/$', views.TramiteDocumentarioMenuTemplateView.as_view(), name='tramite_documentario_menu'),
    url(r'^control-de-asistencia/$', views.ControlAsistenciaTemplateView.as_view(), name='control_asistencia'),
    url(r'^control-de-asistencia/menu/$', views.ControlAsistenciaMenuTemplateView.as_view(), name='control_asistencia_menu'),
    url(r'^tributo-municipal/$', views.TributoMunicipalTemplateView.as_view(), name='control_asistencia'),
]