# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import DiapositivaWeb 

@admin.register(DiapositivaWeb)
class DiapositivaWebAdmin(admin.ModelAdmin):
	list_display   = ('titulo', 'imagen', 'descripcion', 'observacion',
					  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip')
	list_instances = True
	search_fields  = ('titulo',)

	class Meta:
		model = DiapositivaWeb
