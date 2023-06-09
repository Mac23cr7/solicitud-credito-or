from django.db import models

class Cliente(models.Model):
    NOMBREBANCO = (
        ('', 'SELECCIONE BANCO'),
        ('BANESCO', 'BANESCO'),
        ('VENEZUELA', 'VENEZUELA'),
        ('PROVINCIAL', 'PROVINCIAL')
    )
    TIPOPERSONA = (
        ('', 'SELECCIONE TIPO PERSONA'),
        ('NATURAL', 'NATURAL'),
        ('JÚRIDICO', 'JÚRIDICO')
    )
    NACIONALIDAD = (
        ('', 'SELECCIONE NACIONALIDAD'),
        ('E', 'EXTRANJERO'),
        ('V', 'VENEZOLANO')
    )
    id = models.AutoField(primary_key = True)
    nom_ape = models.CharField('Nombre y Apellido Cliente', max_length = 250, null = False, blank = False)
    fec_nacimiento = models.DateField('Fecha de Nacimiento', max_length = 2, null = False, blank = False)
    edad = models.PositiveIntegerField ('Edad del Cliente', null = True, blank = True)
    nacionalidad = models.CharField('Nacionalidad', choices = NACIONALIDAD, max_length = 200, null = False, blank = False)
    direccion = models.CharField('Dirección de Habitación', max_length = 250, null = False, blank = False)
    correo = models.EmailField('Correo Electronico', null = False, blank = False)
    telefono =  models.CharField('Numero Telefonico', max_length = 200, null = True, blank = True)
    tipo_persona = models.CharField('Tipo Persona', choices = TIPOPERSONA,  max_length = 200, null = False, blank = False)
    nombre_banco = models.CharField('Nombre del Banco', choices = NOMBREBANCO,  max_length = 200, null = False, blank = False)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nom_ape
        