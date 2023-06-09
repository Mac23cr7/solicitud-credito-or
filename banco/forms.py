from django import forms
from .models import Banco

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['nombre_banco', 
                'tipo_banco', 
                'direccion']
        labels = {
            'nombre_banco': 'Nombre del Banco',
            'tipo_banco': 'Tipo de Banco',
            'direccion': 'Dirección Banco',
        }
        widgets = {
            'nombre_banco': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del Banco',
                    'id': 'nombre_banco'
                }
            ),
            'tipo_banco': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese tipo de Banco',
                    'id':'tipo_banco'
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese dirección del Banco',
                    'id':'direccion'
                }
            ),
        }