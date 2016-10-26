# -*- encoding: utf-8 -*-
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e542d!9-rai8v4yg1f50$l9!ap-!x!51qze31st4#h&3+ww(g='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #APIS
    'rest_framework',
    'social.apps.django_app.default',
    'embed_video',
    'pure_pagination',
    'widget_tweaks', #Libreria componentes de formularios
    #'sorl.thumbnail', #Recortar imagenes grandes
    #'password_reset',
    #MAIN
    'modulos.apps.ModulosConfig',
    'grupos_modulos.apps.GruposModulosConfig',
    'catalogos_modulos_menus_sub_menus.apps.CatalogosModulosMenusSubMenusConfig',
    'menus.apps.MenusConfig',
    'grupos_menus.apps.GruposMenusConfig',
    'sub_menus.apps.SubMenusConfig',
    #CLASES ABSTRACTAS
    'infos_sistemas.apps.InfosSistemasConfig',
    'ubicaciones.apps.UbicacionesConfig',
    'personas.apps.PersonasConfig',
    #PAGINA WEB
    'index.apps.IndexConfig',
    'tipos_sitios_web.apps.TiposSitiosWebConfig',
    'sitios_web.apps.SitiosWebConfig',
    'redes_sociales.apps.RedesSocialesConfig',
    'catalogos_sitios_web_redes_sociales.apps.CatalogosSitiosWebRedesSocialesConfig',
    'secciones_web.apps.SeccionesWebConfig',
    'tipos_secciones_web.apps.TiposSeccionesWebConfig',
    'tipos_articulos_web.apps.TiposArticulosWebConfig',
    'articulos_web.apps.ArticulosWebConfig',
    'sliders_web.apps.SlidersWebConfig',
    'diapositivas_web.apps.DiapositivasWebConfig',
    #CONTROL ASISTENCIA
    'clases_entidades.apps.ClasesEntidadesConfig',
    'tipos_entidades.apps.TiposEntidadesConfig',
    'documentos_identificaciones.apps.DocumentosIdentificacionesConfig',
    'entidades.apps.EntidadesConfig',
    'sedes.apps.SedesConfig',
    'tipos_areas_funcionales.apps.TiposAreasFuncionalesConfig',
    'tipos_areas.apps.TiposAreasConfig',
    'areas.apps.AreasConfig',
    'paises.apps.PaisesConfig',
    'departamentos.apps.DepartamentosConfig',
    'provincias.apps.ProvinciasConfig',
    'distritos.apps.DistritosConfig',
    'zonas.apps.ZonasConfig',
    'vias.apps.ViasConfig',
    'tipos_empleados.apps.TiposEmpleadosConfig',
    'empleados.apps.EmpleadosConfig',
    'usuarios.apps.UsuariosConfig',
    'estados_civiles.apps.EstadosCivilesConfig',
    'grupos_sanguineos.apps.GruposSanguineosConfig',
    'cargos.apps.CargosConfig',
    'profesiones.apps.ProfesionesConfig',
    'ocupaciones.apps.OcupacionesConfig',
    'grados_instrucciones.apps.GradosInstruccionesConfig',

]

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 1,
    'MARGIN_PAGES_DISPLAYED': 2,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

]

ROOT_URLCONF = 'app_erp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Python Social Auth Context Processors
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',

            ],
        },
    },
]

WSGI_APPLICATION = 'app_erp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
   'default': {
       'ENGINE': "sql_server.pyodbc",
       'HOST': "127.0.0.1",
       'PORT': '1433',
       'USER': "sa",
       'PASSWORD': "S1st3mas",
       'NAME': "App",
       'OPTIONS': {
            'host_is_server': True,
        },
  }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
# Facebook
'social.backends.facebook.FacebookOAuth2',

# Django
'django.contrib.auth.backends.ModelBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
#Configuración de archivos estaticos
STATIC_URL = '/static/'
#MEDIA -> STATIC
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])

STATICFILES_FINDERS = {
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
}

#Activar cache para archivos estaticos
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFileStorage'

#Imagenes, audios y videos
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
MEDIA_URL  = '/media/'

#Configuración de Usuario
AUTH_USER_MODEL = 'usuarios.Usuario'


#Configuracion Autentificacion por Red Social
SOCIAL_AUTH_FACEBOOK_KEY = '1787958631485058'
SOCIAL_AUTH_FACEBOOK_SECRET = '23ce7ad966ca6c817fac1a274ad7be53'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"

#Configuracion de Correo Electronico

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'r.gian.f.carbonell.s@gmail.com'
EMAIL_HOST_PASSWORD = 'S1st3mas'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

SENDSMS_BACKEND = 'sendsms.backends.console.SmsBackend'

#TIEMPO MAXIMO POR DIA PARA RESTABLECER CONTRASEÑA MENDIA LINK
#PASSWORD_RESET_TIMEOUT_DAYS = (1/24)/2
