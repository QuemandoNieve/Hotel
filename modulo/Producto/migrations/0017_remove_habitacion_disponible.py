# Generated by Django 5.1 on 2024-11-22 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0016_habitacion_disponible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitacion',
            name='disponible',
        ),
    ]
