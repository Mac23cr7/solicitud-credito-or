from django import forms
from .models import Credito

class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = ['id_cliente',
                'desc_credito', 
                'pago_minimo', 
                'pago_maximo', 
                'tipo_credito',
                'id_banco',
                'plazo_credito']
        labels = {
            'id_cliente': 'Nombre Cliente del Prestamo',
            'desc_credito': 'Descripción Credito',
            'pago_minimo': 'Pago Minimo',
            'pago_maximo': 'Pago Maximo',
            'tipo_credito': 'Tipo de credito',
            'id_banco': 'Nombre del Banco del Prestamo',
            'plazo_credito': 'Plazo de credito',
        }
        widgets = {
            'id_cliente': forms.Select(
                attrs = {
                    'class':'form-control',
                    'id': 'id_cliente'
                }
            ),
            'desc_credito': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la descripción del Credito',
                    'id': 'desc_credito'
                }
            ),
            'pago_minimo': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese pago minimo',
                    'id':'pago_minimo',
                    'step': '0.00'
                }
            ),
            'pago_maximo': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese pago maximo',
                    'id':'pago_maximo',
                    'step': '0.00'
                }
            ),
            'tipo_credito': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese tipo de Credito',
                    'id':'tipo_credito'
                }
            ),
            'id_banco': forms.Select(
                attrs = {
                    'class':'form-control',
                    'id': 'id_banco'
                }
            ),
            'plazo_credito': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese plazo Credito',
                    'id':'plazo_credito'
                }
            ),
        }
