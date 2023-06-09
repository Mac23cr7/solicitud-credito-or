from django.urls import path
from django.views.generic.base import TemplateView
from .views import ListarCliente, CrearCliente, ActualizarCliente, EliminarCliente

urlpatterns = [
    path('listar_cliente/',ListarCliente.as_view(), name = 'listar_cliente'),
    path('crear_cliente/', CrearCliente.as_view(), name = 'crear_cliente'),
    path('actualizar_cliente/<int:pk>', ActualizarCliente.as_view(), name = 'actualizar_cliente'),
    path('eliminar_cliente/<int:pk>/', EliminarCliente.as_view(), name = 'eliminar_cliente'),
]

""" urls_avanzadas """
urlpatterns += [
    path('inicio_cliente/',TemplateView.as_view(template_name = 'general/clientes/listar_cliente.html'), name = 'inicio_cliente')
]
