# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from infos_sistemas.models import InfoSistema
from sitios_web.models import SitioWeb
from tipos_secciones_web.models import TipoSeccionWeb
from diapositivas_web.models import DiapositivaWeb
from django.template.defaultfilters import slugify


class SeccionWeb(InfoSistema):
	sitio_web 						= models.ForeignKey(SitioWeb)
	tipo_seccion_web 				= models.ForeignKey(TipoSeccionWeb)
	sliders_web						= models.ManyToManyField(DiapositivaWeb, through='sliders_web.SliderWeb')
	
	nombre 	   						= models.CharField(max_length=100, unique=True, db_index=True, help_text='Escribir nombre de la sección web.')
	banner 		   					= models.ImageField(blank=True, 
														upload_to='imagenes_secciones_web', 
														help_text='Subir banner. (Opcional)')
	archivo_video					= models.FileField(
														blank=True,  
														upload_to='archivos_secciones_web', 
													  )
	descripcion    					= models.TextField(blank=True, help_text='(Opcional)')
	observacion    					= models.TextField(blank=True, help_text='(Opcional)')

	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre()
	
	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre		
	def get_nombre(self):
		return self.nombre

	def player_video(self):
		return self.archivo_video.url 

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre()) 
		else:
			slug = slugify(self.get_nombre()) 
			if self.slug != slug:
				self.slug = slug
		super(SeccionWeb, self).save(*args, **kwargs)
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Secciones_Web'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Sección Web' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Secciones Web'


