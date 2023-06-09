from django.urls import path
from django.views.generic.base import TemplateView
from .views import ListarBanco, CrearBanco

urlpatterns = [
    path('listar_banco/',ListarBanco.as_view(), name = 'listar_banco'),
    path('crear_banco/', CrearBanco.as_view(), name = 'crear_banco')
]

""" url_avanzada """
urlpatterns += [
    path('inicio_banco/',TemplateView.as_view(template_name = 'general/bancos/listar_banco.html'), name = 'inicio_banco')
]