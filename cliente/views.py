import json
import datetime
from random import choice
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cliente
from .forms import ClienteForm


class Inicio(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


""" Metodo para listar los clientes """
class ListarCliente(ListView):
    model = Cliente

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = serialize('json', self.get_queryset())
            # print(data)
            return HttpResponse(data, 'application/json')
        else:
            return redirect('cliente:inicio_cliente')


""" Metodo para crear a los clientes """
class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'general/clientes/crear_cliente.html'

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
            return redirect('cliente:inicio_cliente')


""" Metodo para actualizar clientes """
class ActualizarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'general/clientes/actualizar_cliente.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} Actualizado Correctamente!'
                error = 'No hay error'
                response = JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} No se Actualizó Correctamente!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('cliente:inicio_cliente')


""" Metodo para eliminar cliente """
class EliminarCliente(DeleteView):
    model = Cliente
    template_name = 'general/clientes/eliminar_cliente.html'

    def delete(self, request, pk, *args, **kwargs):
        if request.is_ajax():
            object = self.get_object()
            object.delete()
            mensaje = f'{self.model.__name__} Eliminado Correctamente!'
            error = 'No hay error'
            response = JsonResponse({'mensaje':mensaje, 'error':error})
            response.status_code = 201
            return response
        else:
            return redirect('cliente:inicio_cliente')