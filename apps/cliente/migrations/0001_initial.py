# Generated by Django 3.2.5 on 2021-07-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_ape', models.CharField(max_length=250, verbose_name='Nombre y Apellido Cliente')),
                ('fec_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('edad', models.IntegerField(blank=True, null=True, verbose_name='Tipo de Documento')),
                ('nacionalidad', models.CharField(choices=[('E', 'EXTRANJERO'), ('V', 'VENEZOLANO')], max_length=200, verbose_name='Nacionalidad')),
                ('direccion', models.CharField(max_length=250, verbose_name='Dirección de Habitación')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('telefono', models.CharField(blank=True, max_length=200, null=True, verbose_name='Numero Telefonico')),
                ('tipo_persona', models.CharField(choices=[('NATURAL', 'NATURAL'), ('NATURAL', 'NATURAL')], max_length=200, verbose_name='Tipo Persona')),
                ('nombre_banco', models.CharField(choices=[('', 'SELECCIONE BANCO'), ('BANESCO', 'BANESCO'), ('VENEZUELA', 'VENEZUELA'), ('PROVINCIAL', 'PROVINCIAL')], max_length=200, verbose_name='Nombre del Banco')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
