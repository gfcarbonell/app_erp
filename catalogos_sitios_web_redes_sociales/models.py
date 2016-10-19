# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from infos_sistemas.models import InfoSistema
from redes_sociales.models import RedSocial
from sitios_web.models import SitioWeb
from django.template.defaultfilters import slugify


class CatalogoSitioWebRedSocial(InfoSistema):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	sitio_web 						= models.ForeignKey(SitioWeb)
	red_social 						= models.ForeignKey(RedSocial)
	orden 							= models.SmallIntegerField(unique=True)
	url 							= models.URLField(unique=True, db_index=True)
	descripcion		    			= models.TextField(blank=True, null=True, help_text='(Opcional)')
	observacion		   				= models.TextField(blank=True, null=True, help_text='(Opcional)')
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
		super(CatalogoSitioWebRedSocial, self).save(*args, **kwargs)

	def get_nombre(self):
		return ' %s | %s ' %(self.sitio_web.get_nombre(), self.red_social.get_nombre())
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Catalogos_Sitios_Web_Redes_Sociales'
		#Ordenar los registros por un campo especifico
		ordering = ('orden',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Catalogo Sitio Web Red Social' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Catalogos Sitios Web Redes Sociales'