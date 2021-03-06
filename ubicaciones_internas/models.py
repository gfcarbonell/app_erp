from django.db import models

# Create your models here.

class UbicacionInterna(models.Model):
	pabellon						= models.CharField(verbose_name='Pabellón', blank=True, max_length=20, null=True)
	bloque 							= models.CharField(blank=True, max_length=20, null=True)
	sector							= models.CharField(blank=True, max_length=20, null=True)
	zona_secccion					= models.CharField(verbose_name='Zona (Sección)', blank=True, max_length=20, null=True)
	pasadizo 						= models.CharField(blank=True, max_length=20, null=True)
	torre							= models.CharField(blank=True, max_length=20, null=True)
	edificio						= models.CharField(blank=True, max_length=20, null=True)
	piso 							= models.CharField(blank=True, max_length=20, null=True)
	interior						= models.CharField(blank=True, max_length=20, null=True)
	numero 							= models.CharField(blank=True, max_length=20, null=True)
	denominacion					= models.CharField(verbose_name='Denominación', blank=True, max_length=255, null=True)
	referencia						= models.TextField(blank=True, null=True)

	class Meta:
		abstract = True
