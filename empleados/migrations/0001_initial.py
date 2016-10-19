# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 19:15
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ocupaciones', '0001_initial'),
        ('estados_civiles', '0001_initial'),
        ('grupos_sanguineos', '0001_initial'),
        ('tipos_empleados', '0001_initial'),
        ('distritos', '0004_auto_20161003_2304'),
        ('cargos', '0001_initial'),
        ('zonas', '0002_auto_20161003_2304'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grados_instrucciones', '0001_initial'),
        ('areas', '0004_auto_20161005_1258'),
        ('vias', '0002_auto_20161003_2304'),
        ('profesiones', '0001_initial'),
        ('documentos_identificaciones', '0004_auto_20161005_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('ultimo_nombre_host', models.CharField(max_length=255)),
                ('ultimo_direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('sector', models.CharField(blank=True, max_length=20, null=True)),
                ('zona_secccion', models.CharField(blank=True, max_length=20, null=True)),
                ('pabellon', models.CharField(blank=True, max_length=20, null=True)),
                ('bloque', models.CharField(blank=True, max_length=20, null=True)),
                ('pasadizo', models.CharField(blank=True, max_length=20, null=True)),
                ('torre', models.CharField(blank=True, max_length=20, null=True)),
                ('edificio', models.CharField(blank=True, max_length=20, null=True)),
                ('departamento', models.CharField(blank=True, max_length=20, null=True)),
                ('apartamento', models.CharField(blank=True, max_length=20, null=True)),
                ('piso', models.CharField(blank=True, max_length=20, null=True)),
                ('interior', models.CharField(blank=True, max_length=20, null=True)),
                ('cuadra', models.CharField(blank=True, max_length=20, null=True)),
                ('manzana', models.CharField(blank=True, max_length=20, null=True)),
                ('numero', models.CharField(blank=True, max_length=20, null=True)),
                ('etapa', models.CharField(blank=True, max_length=20, null=True)),
                ('lote', models.CharField(blank=True, max_length=20, null=True)),
                ('sub_lote', models.CharField(blank=True, max_length=20, null=True)),
                ('kilometro', models.CharField(blank=True, max_length=20, null=True)),
                ('denominacion', models.CharField(blank=True, max_length=255, null=True)),
                ('referencia', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_persona', models.CharField(choices=[('Jurídica', 'Jurídica'), ('Natural', 'Natural')], help_text='Seleccionar tipo de persona.', max_length=8)),
                ('apellido_paterno', models.CharField(db_index=True, help_text='Escribir apellido paterno.', max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)])),
                ('apellido_materno', models.CharField(db_index=True, help_text='Escribir apellido materno.', max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)])),
                ('nombre', models.CharField(db_index=True, help_text='Escribir nombre(s).', max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Nombre(s)')),
                ('numero_documento_identificacion', models.CharField(db_index=True, help_text='Escribir número documento identificación.', max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(20)], verbose_name='Número documento identificación')),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=9, verbose_name='Género')),
                ('fotografia', models.ImageField(blank=True, help_text='Subir fotografia (Opcional).', null=True, upload_to='', verbose_name='Fotografía')),
                ('hijo', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False, verbose_name='¿Hijo(s)?')),
                ('numero_hijo', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Escribir número(s) de hijo(s).', verbose_name='Número de hijo(s)')),
                ('telefono', models.CharField(blank=True, help_text='(Opcional).', max_length=20, null=True, verbose_name='Télefono (Personal)')),
                ('celular', models.CharField(blank=True, help_text='(Opcional).', max_length=20, null=True, verbose_name='Celular (Personal)')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.EmailValidator(), django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Correo electrónico (Personal)')),
                ('observacion_persona', models.TextField(blank=True, help_text='Escribir observación de la persona (Opcional).', null=True, verbose_name='Observación (Persona)')),
                ('nombre_direccion', models.CharField(db_index=True, help_text='Escribir nombre de la dirección.', max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Nombre dirección')),
                ('observacion_dirección', models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Observación (Dirección)')),
                ('fecha_inicio_contratacion', models.DateField(help_text='Seleccionar fecha de inicio de contratación del empleado.')),
                ('fecha_fin_contratacion', models.DateField(blank=True, help_text='Seleccionar fecha de final de contratación del empleado.', null=True)),
                ('fecha_cese', models.DateTimeField(blank=True, help_text='Seleccionar fecha de cese del empleado.', null=True)),
                ('descripcion', models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Descripción')),
                ('observacion', models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Observación')),
                ('activo', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areas.Area')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargos.Cargo')),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados_empleado_related', to='distritos.Distrito')),
                ('documento_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados_empleado_related', to='documentos_identificaciones.DocumentoIdentificacion', verbose_name='Documento identificación')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados_empleado_related', to='estados_civiles.EstadoCivil')),
                ('grado_instruccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grados_instrucciones.GradoInstruccion')),
                ('grupo_sanguineo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados_empleado_related', to='grupos_sanguineos.GrupoSanguineo', verbose_name='Grupo sanguíneo')),
                ('ocupacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocupaciones.Ocupacion')),
                ('profesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesiones.Profesion')),
                ('tipo_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipos_empleados.TipoEmpleado')),
                ('ultimo_usuario_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados_empleado_related', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_empleados_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('via', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados_empleado_related', to='vias.Via')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados_empleado_related', to='zonas.Zona')),
            ],
            options={
                'ordering': ('apellido_paterno',),
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleados',
            },
        ),
    ]
