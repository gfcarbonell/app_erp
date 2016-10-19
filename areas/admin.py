# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Area 
from infos_sistemas.admin import InfoSistemaAdmin


@admin.register(Area)
class AreaAdmin(InfoSistemaAdmin):
	list_display   = ( 'sede', 'area_dependiente', 'tipo_area_funcional', 'tipo_area', 'nombre', 'siglas', 'email', 'fax_interno',
						'anexo_interno', 'mision', 'vision', 'logotipo', 'fecha_creacion', 'fecha_cese', 'descripcion', 'observacion',
						'activo',
					  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Area
