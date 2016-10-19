# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from infos_sistemas.models import InfoSistema
from django.template.defaultfilters import slugify
from embed_video.fields import EmbedVideoField


class DiapositivaWeb(InfoSistema):
	titulo 	   						= models.CharField(max_length=100, unique=True, db_index=True, help_text='Escribir el título de la diapositiva web.')
	imagen 		   					= models.ImageField(upload_to='imagenes_diapostivas_web', 
														help_text='Subir imagen de la diapositiva web. (Opcional)')
	video  							= EmbedVideoField(
														blank=True,  
													  )
	archivo  						= models.FileField(
														blank=True,  
														upload_to='archivos_articulos_web', 
													  )
	descripcion    					= models.TextField(blank=True, help_text='(Opcional)')
	observacion    					= models.TextField(blank=True, help_text='(Opcional)')
	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_titulo()
	
	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre	

	def player_video(self):
		return self.archivo.url 

	def player_tag_video(self):
		return """
				<video loop autoplay>
				    <source src="%s" type="video/mp4">
					 Your browser does not support the video tag.
				</video>
			   """ % self.archivo.url
	player_tag_video.allow_tags = True		   

	def get_titulo(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_titulo()) 
		else:
			slug = slugify(self.get_titulo()) 
			if self.slug != slug:
				self.slug = slug
		super(DiapositivaWeb, self).save(*args, **kwargs)
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Diapositivas_Web'
		#Ordenar los registros por un campo especifico
		ordering = ('titulo',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Diapositiva Web' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Diapositivas Web'


