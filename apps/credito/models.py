from django.db import models
from apps.banco.models import Banco
from apps.cliente.models import Cliente

class Credito(models.Model):
    TIPOCREDITO = (
        ('', 'SELECCIONE CREDITO'),
        ('AUTOMOTRIZ', 'AUTOMOTRIZ'),
        ('HIPOTECARIO', 'HIPOTECARIO'),
        ('COMERCIALES', 'COMERCIALES')
    )
    id = models.AutoField(primary_key = True)
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, null = False, blank = False)
    desc_credito = models.CharField('Descripción del Credito', max_length = 200, null = False, blank = False)
    pago_minimo = models.FloatField('Pago Minimo', default=0, null = False, blank = False)
    pago_maximo = models.FloatField('Pago Maximo', default=0, null = False, blank = False)
    plazo_credito = models.IntegerField('Plazo Credito', null = False, blank = False)
    fecha_registro = models.DateField('Fecha de Registro', auto_now = False, auto_now_add = True, null = False, blank = False)
    id_banco = models.ForeignKey(Banco, on_delete = models.CASCADE, null = False, blank = False)
    tipo_credito = models.CharField('Tipo Credito', choices = TIPOCREDITO, max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Credito'
        verbose_name_plural = 'Creditos'

    def __str__(self):
        return self.desc_credito

