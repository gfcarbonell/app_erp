# -*- encoding: utf-8 -*-
from django.db import models
from vias.models import Via
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class Ubicacion_1(models.Model):
	CHOICES_PREFIJO_BIS 			= ((0, ''), (1, 'BIS'))
	CHOICES_CUADRANTE 				= (
										('-' , ''),
										('Este' , 'Este'),
										('Norte', 'Norte'),
										('Oeste', 'Oeste'),
										('Sur'  , 'Sur'),
									  )

	via = models.ForeignKey(Via)
	nombre_via					  				= models.CharField(
														verbose_name='Nombre dirección',
														max_length=255,
														validators=[
															        MinLengthValidator(1),
															        MaxLengthValidator(255),
															    ],
														db_index=True,
														help_text='Escribir nombre de la vía.')
	numero_letra_asociada_nombre_via 	       = models.CharField(blank=True, max_length=20, null=True)
	prefijo_bis_via 			   			   = models.BooleanField(default=0, choices = CHOICES_PREFIJO_BIS)
	numero_letra_asociada_prefijo_bis_via 	   = models.CharField(blank=True, max_length=20, null=True)
	cuadrante_vial 							   = models.BooleanField(default=0, choices = CHOICES_PREFIJO_BIS)
	numero_via_generadora 							   = models.PositiveSmallIntegerField(
														blank=True,
														default = 0,
														validators=[
															        MinValueValidator(0),
															        MaxValueValidator(10),
															    ],
														)
	numero_letra_asociada_numero_via_generadora 	   	= models.CharField(blank=True, max_length=20, null=True)
	prefijo_bis_via_generadora 	   			  			= models.BooleanField(default=0, choices = CHOICES_PREFIJO_BIS)
	numero_letra_asociada_prefijo_bis_via_generadora 	= models.CharField(blank=True, max_length=20, null=True)
	numero_placa							  		    = models.PositiveSmallIntegerField(
															blank=True,
															default = 0,
															validators=[
																        MinValueValidator(0),
																        MaxValueValidator(10),
																    ],
															)
	cuadrante_via_generadora	 					   = models.BooleanField(default=0, choices = CHOICES_PREFIJO_BIS)
	class Meta:
		abstract = True

class Ubicacion(models.Model):
	sector							= models.CharField(blank=True, max_length=20, null=True)
	zona_secccion					= models.CharField(verbose_name='Zona (Sección)', blank=True, max_length=20, null=True)
	pabellon						= models.CharField(verbose_name='Pabellón', blank=True, max_length=20, null=True)
	bloque 							= models.CharField(blank=True, max_length=20, null=True)
	pasadizo 						= models.CharField(blank=True, max_length=20, null=True)
	torre							= models.CharField(blank=True, max_length=20, null=True)
	edificio						= models.CharField(blank=True, max_length=20, null=True)
	departamento					= models.CharField(blank=True, max_length=20, null=True)
	apartamento						= models.CharField(blank=True, max_length=20, null=True)
	piso 							= models.CharField(blank=True, max_length=20, null=True)
	interior						= models.CharField(blank=True, max_length=20, null=True)
	cuadra							= models.CharField(blank=True, max_length=20, null=True)
	manzana							= models.CharField(blank=True, max_length=20, null=True)
	numero 							= models.CharField(blank=True, max_length=20, null=True)
	etapa							= models.CharField(blank=True, max_length=20, null=True)
	lote							= models.CharField(blank=True, max_length=20, null=True)
	sub_lote						= models.CharField(blank=True, max_length=20, null=True)
	kilometro						= models.CharField(blank=True, max_length=20, null=True)
	denominacion					= models.CharField(verbose_name='Denominación', blank=True, max_length=255, null=True)
	referencia						= models.TextField(blank=True, null=True)

	class Meta:
		abstract = True
