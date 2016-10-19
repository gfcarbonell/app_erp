# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from secciones_web.models import SeccionWeb
from sliders_web.models import SliderWeb
from entidades.models import Entidad


class IndexTemplateView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexTemplateView, self).get_context_data(**kwargs)	
		is_auth  = False 
		username = None
		id_usuario = None
		sliders_web = SliderWeb.objects.order_by('orden').all()
		entidad = Entidad.objects.get(nombre = "Municipalidad Distrital de San Andrés")
		seccion_web_inicio = SeccionWeb.objects.get(nombre='Inicio')

		if self.request.user.is_authenticated():
			id_usuario  = self.get_user_id()
			is_auth 	= True
			username    = self.get_username()

		data = {
			'id_usuario' : id_usuario,
			'is_auth'	 : is_auth,
			'username'   : username,
			'sliders_web': sliders_web,
			'entidad'	 : entidad,
			'seccion_web_inicio': seccion_web_inicio,
			}

		

		context.update(data)
		return context

	def get_user_id(self):
		return self.request.user.id 

	def get_username(self):
		return self.request.user.username

