# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from catalogos_modulos_menus_sub_menus.models import CatalogoModuloMenuSubMenu


class CatalagoModuloMenuTemplateView(TemplateView):
	template_name = 'catologo_modulo_menu.html'

	def get_context_data(self, **kwargs):
		context = super(CatalagoModuloMenuTemplateView, self).get_context_data(**kwargs)	
		is_auth  = False 
		username = None
		id_usuario = None
		boton_menu = False
		if self.request.user.is_authenticated():
			id_usuario  = self.get_user_id()
			is_auth 	= True
			username    = self.get_username()
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.filter(menu__nombre='main')
		data = {
			'id_usuario' : id_usuario,
			'is_auth'	 : is_auth,
			'username'   : username,
			'catalogos_modulos_menus':catalogos_modulos_menus,
			'boton_menu':boton_menu,
			}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id 

	def get_username(self):
		return self.request.user.username


class TramiteDocumentarioTemplateView(TemplateView):
	template_name = 'tramite_documentario.html'

	def get_context_data(self, **kwargs):
		context = super(TramiteDocumentarioTemplateView, self).get_context_data(**kwargs)	
		is_auth  = False 
		username = None
		id_usuario = None
		boton_menu = False
		if self.request.user.is_authenticated():
			id_usuario  = self.get_user_id()
			is_auth 	= True
			username    = self.get_username()
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.get(modulo__slug='tramite-documentario', menu__slug='main')
		data = {
			'id_usuario' 			 : id_usuario,
			'is_auth'	 			 : is_auth,
			'username'  			 : username,
			'catalogos_modulos_menus':catalogos_modulos_menus,
			'boton_menu'			 : boton_menu,
			}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id 

	def get_username(self):
		return self.request.user.username


class TramiteDocumentarioMenuTemplateView(TemplateView):
	template_name = 'tramite_documentario_menu.html'

	def get_context_data(self, **kwargs):
		context = super(TramiteDocumentarioMenuTemplateView, self).get_context_data(**kwargs)	
		is_auth  = False 
		username = None
		id_usuario = None
		
		if self.request.user.is_authenticated():
			id_usuario  = self.get_user_id()
			is_auth 	= True
			username    = self.get_username()
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.filter(modulo__slug='tramite-documentario').exclude(menu__slug ='main')
			catalogos_modulos 	    = CatalogoModuloMenuSubMenu.objects.filter(menu__slug='main')
		data = {
			'id_usuario' 			  : id_usuario,
			'is_auth'	 			  : is_auth,
			'username'  			  : username,
			'catalogos_modulos'		  : catalogos_modulos,
			'catalogos_modulos_menus' : catalogos_modulos_menus,
			}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id 

	def get_username(self):
		return self.request.user.username


class ControlAsistenciaTemplateView(TemplateView):
	template_name = 'control_asistencia.html'

	def get_context_data(self, **kwargs):
		context = super(ControlAsistenciaTemplateView, self).get_context_data(**kwargs)	
		is_auth  = False 
		username = None
		id_usuario = None
		boton_menu = False
		if self.request.user.is_authenticated():
			id_usuario  = self.get_user_id()
			is_auth 	= True
			username    = self.get_username()
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.get(modulo__slug='control-de-asistencia', menu__slug='main')
		data = {
			'id_usuario' 			 : id_usuario,
			'is_auth'	 			 : is_auth,
			'username'  			 : username,
			'catalogos_modulos_menus':catalogos_modulos_menus,
			'boton_menu':boton_menu,
			}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id 

	def get_username(self):
		return self.request.user.username

class ControlAsistenciaMenuTemplateView(TemplateView):
	template_name = 'control_asistencia_menu.html'

	def get_context_data(self, **kwargs):
		context = super(ControlAsistenciaMenuTemplateView, self).get_context_data(**kwargs)	
		is_auth  = False 
		username = None
		id_usuario = None
		
		if self.request.user.is_authenticated():
			id_usuario  = self.get_user_id()
			is_auth 	= True
			username    = self.get_username()
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.filter(modulo__slug='control-de-asistencia').exclude(menu__slug ='main')
			catalogos_modulos 	    = CatalogoModuloMenuSubMenu.objects.filter(menu__slug='main')
		data = {
			'id_usuario' 			  : id_usuario,
			'is_auth'	 			  : is_auth,
			'username'  			  : username,
			'catalogos_modulos'		  : catalogos_modulos,
			'catalogos_modulos_menus' : catalogos_modulos_menus,
			}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id 

	def get_username(self):
		return self.request.user.username

class TributoMunicipalTemplateView(TemplateView):
	template_name = 'tributo_municipal.html'

	def get_context_data(self, **kwargs):
		context = super(TributoMunicipalTemplateView, self).get_context_data(**kwargs)	
		is_auth  = False 
		username = None
		id_usuario = None
		boton_menu = False
		if self.request.user.is_authenticated():
			id_usuario  = self.get_user_id()
			is_auth 	= True
			username    = self.get_username()
			catalogos_modulos_menus = CatalogoModuloMenuSubMenu.objects.get(modulo__slug='tributo-municipal', menu__slug='main')
		data = {
			'id_usuario' 			 : id_usuario,
			'is_auth'	 			 : is_auth,
			'username'  			 : username,
			'catalogos_modulos_menus': catalogos_modulos_menus,
			'boton_menu'			 : boton_menu,
			}

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id 

	def get_username(self):
		return self.request.user.username