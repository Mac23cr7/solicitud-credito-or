from django.urls import path
from django.views.generic.base import TemplateView
from .views import ListarCredito, CrearCredito

urlpatterns = [

    path('listar_credito/',ListarCredito.as_view(), name = 'listar_credito'),
    path('crear_credito/', CrearCredito.as_view(), name = 'crear_credito')
]

""" url_avanzada """
urlpatterns += [
    path('inicio_credito/',TemplateView.as_view(template_name = 'listar_credito.html'), name = 'inicio_credito')
]