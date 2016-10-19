# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from infos_sistemas.models import InfoSistema
from tipos_articulos_web.models import TipoArticuloWeb
from secciones_web.models import SeccionWeb
from django.template.defaultfilters import slugify
from embed_video.fields import EmbedVideoField


class ArticuloWeb(InfoSistema):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	seccion_web 					= models.ForeignKey(SeccionWeb)
	tipos_articulo_web 	 			= models.ForeignKey(TipoArticuloWeb)
	titulo 	   						= models.CharField(max_length=255, unique=True, db_index=True, help_text='Escribir nombre del articulo web.')
	slogan 	   						= models.CharField(max_length=255, unique=True, db_index=True,)
	imagen 		   					= models.ImageField(blank=True, 
														upload_to='imagenes_articulos_web', 
														default='default/No_Image_1.png',
														help_text='Subir imagen del tipo de articulo web. (Opcional)')
	video  							= EmbedVideoField(
														blank=True,  
													  )
	descripcion    					= models.TextField(blank=True, help_text='(Opcional)')
	observacion    					= models.TextField(blank=True, help_text='(Opcional)')
	activo 							= models.BooleanField(default=True, choices=BOOL_ACTIVO)
	fecha_publicacion				= models.DateField(verbose_name='Fecha publicación', blank=True, null=True)
	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_titulo()
	
	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre	

	def get_titulo(self):
		return self.titulo
	

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre()) 
		else:
			slug = slugify(self.get_nombre()) 
			if self.slug != slug:
				self.slug = slug
		super(ArticuloWeb, self).save(*args, **kwargs)
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Articulos_Web'
		#Ordenar los registros por un campo especifico
		ordering = ('titulo',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Articulo Web' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Articulos Web'


