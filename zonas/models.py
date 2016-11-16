# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from infos_sistemas.models import InfoSistema
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class Zona(InfoSistema):
	nombre 	   						= models.CharField(
									  max_length=100,
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(100),
								  		    ],
									  unique=True,
									  db_index=True,
									  help_text='Escribir el nombre de la zona.')

	abreviatura						= models.CharField(
									  max_length=10,
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(10),
								  		    ],
									  db_index=True,)
	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre
	def get_nombre(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre())
		else:
			slug = slugify(self.get_nombre())
			if self.slug != slug:
				self.slug = slug
		super(Zona, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Zonas'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Zona'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Zonas'
