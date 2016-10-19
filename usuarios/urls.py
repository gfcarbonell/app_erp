# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.core.urlresolvers  import reverse_lazy


"""
    url(r'^password-reset/$', password_reset,  
      {
       'template_name'       : 'password_reset_form.html',
       'email_template_name' : 'password_reset_email.html',
       'password_reset_form' : UsuarioPasswordResetForm,
       'post_reset_redirect' : '/usuario/password-reset/done',
       },

      name='password_reset'),  

    url(r'^password-reset/done/$',password_reset_done, 
        {'template_name': 'password_reset_done.html',},
        name='password_reset_done'),

    url (r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)-(?P<token>.+)/$', password_reset_confirm, 
        {
          'template_name'       : 'password_reset_confirm.html',  
          'post_reset_redirect' : '/usuario/password-reset/done',
        }, 

         name='password_reset_confirm' ),

    url(r'^password-reset/complete/$',password_reset_complete, 
        {'template_name': 'password_reset_complete.html',},
        name='password_reset_complete'),

    url(r'^password-changed/$', password_change,  
      {
       'template_name'       : 'password_change_form.html',
       'post_change_redirect': 'password_change_done.html', 
       'password_change_form':  UsuarioPasswordChangeForm
       },

      name='password_changed'),   

    url(r'^password_changed/done$', password_change_done, 
        {'template_name': 'password_change_done.html',},
        name='password_change_done'),
"""

urlpatterns = [
    url(r'^control-de-asistencia/usuarios/$', views.UsuarioControlListView.as_view(), name='control'),
    url(r'^control-de-asistencia/usuario/nuevo/$', views.UsuarioCreateView.as_view(), name='create'),
    url(r'^control-de-asistencia/usuario/(?P<slug>[\w-]+)/modificar/$', views.UsuarioUpdateView.as_view(), name='update'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'), 
    url(r'^login/$', views.LoginView.as_view(), name='login'), 

]