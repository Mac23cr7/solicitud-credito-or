# Generated by Django 3.2.5 on 2021-07-22 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credito', '0002_auto_20210722_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='plazo_credito',
            field=models.IntegerField(verbose_name='Plazo Credito'),
        ),
    ]
