# Generated by Django 3.2.5 on 2021-07-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(blank=True, null=True, verbose_name='Edad del Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nacionalidad',
            field=models.CharField(choices=[('', 'SELECCIONE NACIONALIDAD'), ('E', 'EXTRANJERO'), ('V', 'VENEZOLANO')], max_length=200, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_persona',
            field=models.CharField(choices=[('', 'SELECCIONE TIPO PERSONA'), ('NATURAL', 'NATURAL'), ('JÚRIDICO', 'JÚRIDICO')], max_length=200, verbose_name='Tipo Persona'),
        ),
    ]
