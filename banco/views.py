from random import choice
from django.db.models import base
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, CreateView
from .models import Banco
from .forms import BancoForm


class Inicio(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())



""" Metodo para listar los bancos de la BD """
class ListarBanco(ListView):
    model = Banco

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = serialize('json', self.get_queryset())
            # print(data)
            return HttpResponse(data, 'application/json')
        else:
            return redirect('banco:inicio_banco')


""" Metodo para crear un nuevo banco """
class CrearBanco(CreateView):
    model = Banco
    form_class = BancoForm
    template_name = 'crear_banco.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} Registrado Correctamente!'
                error = 'No hay error'
                response = JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} No se Registró Correctamente!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('banco:inicio_banco')

