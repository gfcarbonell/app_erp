# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from infos_sistemas.models import InfoSistema
from secciones_web.models import SeccionWeb
from diapositivas_web.models import DiapositivaWeb
from django.template.defaultfilters import slugify


class SliderWeb(InfoSistema):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	seccion_web						= models.ForeignKey(SeccionWeb)
	diapositiva_web					= models.ForeignKey(DiapositivaWeb)
	orden 							= models.SmallIntegerField()
	activo 							= models.BooleanField(default=True, choices=BOOL_ACTIVO)
	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre()
	
	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre		

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre()) 
		else:
			slug = slugify(self.get_nombre()) 
			if self.slug != slug:
				self.slug = slug
		super(SliderWeb, self).save(*args, **kwargs)	

	def get_nombre(self):
		return ' %s | %s ' %(self.seccion_web.get_nombre(), self.diapositiva_web.get_titulo())
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Sliders_Web'
		#Ordenar los registros por un campo especifico
		ordering = ('orden',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Slider Web' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Sliders Web'