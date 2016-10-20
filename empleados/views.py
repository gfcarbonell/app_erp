# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, ListView
from .models import Empleado
from .forms import EmpleadoModelForm, EmpleadoUsuarioForm
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin

class EmpleadoCreateView(CreateView):
    template_name = 'empleado_create.html'
    form_class    	  = EmpleadoUsuarioForm
    model         = Empleado
    success_url   = reverse_lazy('empleado:control')

    def form_valid(self, form):
        user = form['model_form_usuario'].save(commit=False)
        user.usuario_creador      = self.request.user
        user.ultimo_usuario_editor = user.usuario_creador
        try:
            user.nombre_host = socket.gethostname()
            user.ultimo_nombre_host = user.nombre_host
        except:
           user.nombre_host  = 'localhost'
           user.ultimo_nombre_host = user.nombre_host
        user.direccion_ip    = socket.gethostbyname(socket.gethostname())
        user.ultimo_direccion_ip =  socket.gethostbyname(socket.gethostname())


        empleado = form['model_form_empleado'].save(commit=False)
        empleado.tipo_persona = 'Natural'
        if empleado.numero_hijo is None:
            empleado.numero_hijo = 0

        user.save()

        empleado.usuario = user
        empleado.usuario_creador      = self.request.user
        empleado.ultimo_usuario_editor = empleado.usuario_creador
        try:
            empleado.nombre_host = socket.gethostname()
            empleado.ultimo_nombre_host = empleado.nombre_host
        except:
           empleado.nombre_host  = 'localhost'
           empleado.ultimo_nombre_host = empleado.nombre_host
        empleado.direccion_ip    = socket.gethostbyname(socket.gethostname())
        empleado.ultimo_direccion_ip =  socket.gethostbyname(socket.gethostname())

        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)

    def get_context_data(self, **kwarg):
        context     = super(EmpleadoCreateView, self).get_context_data(**kwarg)
        is_auth  = False
        username = None
        id_usuario = None
        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()
        data = {
            'id_usuario' : id_usuario,
            'is_auth'    : is_auth,
            'username'   : username,
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id

    def get_username(self):
        return self.request.user.username


class EmpleadoControlListView(PaginationMixin, ListView):
    model         = Empleado
    template_name = 'empleados.html'
    paginate_by   = 10

    def get_context_data(self, **kwarg):
        context     = super(EmpleadoControlListView, self).get_context_data(**kwarg)
        is_auth  = False
        username = None
        id_usuario = None
        boton_menu     = False
        total_registro = self.model.objects.count()

        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()

        data = {
            'id_usuario'    : id_usuario,
            'is_auth'       : is_auth,
            'username'      : username,
            'boton_menu'    : boton_menu,
            'total_registro': total_registro,
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id

    def get_username(self):
        return self.request.user.username


    def get(self, request, *args, **kwargs):
        if request.GET.get('search_registro', None):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return super(EmpleadoControlListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('search_registro', None):
            queryset = self.model.objects.filter(
                        Q(apellido_paterno__icontains=self.request.GET.get('search_registro', None))
                        |Q(apellido_materno__icontains=self.request.GET.get('search_registro', None))
                        |Q(nombre__icontains=self.request.GET.get('search_registro', None))
                        |Q(numero_documento_identificacion__icontains=self.request.GET.get('search_registro', None))
                        |Q(area__nombre__icontains=self.request.GET.get('search_registro', None))
                    )
        else:
            queryset = super(EmpleadoControlListView, self).get_queryset()
        return queryset
