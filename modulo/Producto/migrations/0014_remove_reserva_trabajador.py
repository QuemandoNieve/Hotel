# Generated by Django 5.0.4 on 2024-11-19 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0013_rename_fecha_agregada_reservaregalia_fecha_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='trabajador',
        ),
    ]
