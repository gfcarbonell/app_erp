# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import SliderWeb 

@admin.register(SliderWeb)
class SliderWebAdmin(admin.ModelAdmin):
	list_display   = ('seccion_web', 'diapositiva_web', 'orden', 'activo',
					  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = SliderWeb
