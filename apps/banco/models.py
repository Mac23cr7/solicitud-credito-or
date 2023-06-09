from django.db import models

class Banco(models.Model):
    TIPOBANCO = (
        ('PRIVADO', 'PRIVADO'),
        ('GOBIERNO', 'GOBIERNO')
    )
    id = models.AutoField(primary_key = True)
    nombre_banco = models.CharField('Nombre del Banco', max_length = 200, null = False, blank = False)
    tipo_banco = models.CharField('Tipo Banco', choices = TIPOBANCO, max_length = 100, null = False, blank = False)
    direccion = models.CharField('Dirección de Banco', max_length = 200, null = False, blank = False)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'

    def __str__(self):
        return self.nombre_banco
