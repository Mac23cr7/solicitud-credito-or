import json
import datetime
from random import choice
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import  Credito
from .forms import CreditoForm


class Inicio(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


""" Metodo para listar los creditos de la BD """
class ListarCredito(ListView):
    model = Credito

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            objectQuerySet = Credito.objects.all()
            list = []
            for row in objectQuerySet:
                list.append({'pk':row.id,
                            'id_cliente':row.id_cliente.nom_ape,
                            'desc_credito':row.desc_credito,
                            'pago_minimo':row.pago_minimo,
                            'pago_maximo':row.pago_maximo,
                            'tipo_credito':row.tipo_credito,
                            'id_banco':row.id_banco.nombre_banco,
                            'plazo_credito':row.plazo_credito
                            })
            recipe_list_json = json.dumps(list)
            return HttpResponse(recipe_list_json, 'application/json')
        else:
            return redirect('credito:inicio_credito')



""" Metodo para Crear Credito """
class CrearCredito(CreateView):
    model = Credito
    form_class = CreditoForm
    template_name = 'general/creditos/crear_credito.html'

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
            return redirect('credito:inicio_credito')