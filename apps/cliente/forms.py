from django import forms
from .models import Cliente

class DateInput(forms.DateInput):
    input_type = 'date'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nom_ape', 
                'fec_nacimiento', 
                'edad', 
                'nacionalidad', 
                'direccion', 
                'correo',
                'telefono',
                'tipo_persona',
                'nombre_banco']
        labels = {
            'nom_ape': 'Nombre Completo Cliente',
            'fec_nacimiento': 'Fecha de Nacimiento',
            'edad': 'Edad del Cliente',
            'nacionalidad': 'Nacionalidad',
            'direccion': 'Dirección',
            'correo': 'Correo Electronico',
            'telefono': 'Numero Telefonico',
            'tipo_persona': 'Tipo de Persona',
            'nombre_banco': 'Nombre Banco',
        }
        widgets = {
            'nom_ape': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre completo del Cliente',
                    'id': 'nombres'
                }
            ),
            'fec_nacimiento': DateInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'edad':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese edad del Cliente',
                    'id':'edad'
                }
            ),
            'nacionalidad': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese Nacionalidad del Cliente',
                    'id':'nacionalidad'
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese dirección del Cliente',
                    'id':'direccion'
                }
            ),
            'correo': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese Correo Electronico',
                    'id':'correo'
                }
            ),
              'telefono': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese Numero Telefonico',
                    'id':'telefono'
                }
            ),
            'tipo_persona': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese Tipo Persona Cliente',
                    'id':'tipo_persona'
                }
            ),
            'nombre_banco': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese Nombre Banco del Cliente',
                    'id':'nombre_banco'
                }
            ),

        }