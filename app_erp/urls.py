# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
#ViewSet
#CONTROL ASISTENCIA
from usuarios.views import UsuarioViewSet, PermissionViewSet, GroupViewSet, ContentTypeViewSet
from documentos_identificaciones.views import DocumentoIdentificacionViewSet
#SITIO WEB
from tipos_sitios_web.views import TipoSitioWebViewSet
from sitios_web.views import SitioWebViewSet
from tipos_secciones_web.views import TipoSeccionWebViewSet
from secciones_web.views import SeccionWebViewSet
from sliders_web.views import SliderWebViewSet
from diapositivas_web.views import DiapositivaWebViewSet

router = routers.DefaultRouter()

#MODULOS - PAGINA WEB
router.register(r'tipos_sitios_web', TipoSitioWebViewSet)
router.register(r'sitios_web', SitioWebViewSet)
router.register(r'tipos_secciones_web', TipoSeccionWebViewSet)
router.register(r'secciones_web', SeccionWebViewSet)
router.register(r'sliders_web', SliderWebViewSet)
router.register(r'diapositivas_web', DiapositivaWebViewSet)
#MODULOS - CONTROL ASISTENCIA
router.register(r'usuarios', UsuarioViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'content_type', ContentTypeViewSet)
router.register(r'documentos_identificaciones', DocumentoIdentificacionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #MAIN
    ##################################################################################
    #CATALOGOS MODULOS MENUS
    url(r'^',                           include('catalogos_modulos_menus_sub_menus.urls', namespace='catalogo_modulo_menu_sub_menu')),


    #CONTROL ASISTENCIA
    ##################################################################################
    #USUARIOS
    url(r'^control-de-asistencia/',     include('empleados.urls', namespace='empleado')),
    url(r'^', 	                        include('usuarios.urls', namespace='usuario')),

    #SITIO WEB
    ##################################################################################
    url(r'^',                           include('index.urls', namespace='index')),

    #REST
    url(r'^api/', 						include(router.urls)),

    # Python Social Auth URLs
	url('', include('social.apps.django_app.urls', namespace='social')),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
