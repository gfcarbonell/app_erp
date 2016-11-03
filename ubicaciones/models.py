# -*- encoding: utf-8 -*-
from django.db import models
from vias.models import Via
from nucleos_residenciales.models import NucleoResidencial
from divisiones_areas_urbanas.models import DivisionAreaUrbana
from ubicaciones_predios.models import UbicacionPredio
from tipos_predios.models import TipoPredio
from complementos_ubicaciones_predios.models import ComplementoUbicacionPredio
from distritos.models import Distrito
from zonas.models import Zona

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from infos_sistemas.validators import valid_extension


class Ubicacion(models.Model):
    distrito 				= models.ForeignKey(Distrito, related_name='%(app_label)s_%(class)s_related')
    zona					= models.ForeignKey(Zona, related_name='%(app_label)s_%(class)s_related')
    via						= models.ForeignKey(Via, related_name='%(app_label)s_%(class)s_related',)
    nombre_zona_via  = models.CharField(
    								verbose_name='Nombre',
    								max_length=255,
    								validators=[
    									        MinLengthValidator(1),
    									        MaxLengthValidator(255),
    									    ],
    								db_index=True,
    								help_text='Escribir nombre (Zona/Vía).')
    denominacion	= models.CharField(verbose_name='Denominación', blank=True, max_length=255, null=True, help_text='(Opcional).')
    observacion_zona_via = models.TextField( verbose_name='Observación (Zona/Vía)', blank=True, null=True, help_text='(Opcional).')
