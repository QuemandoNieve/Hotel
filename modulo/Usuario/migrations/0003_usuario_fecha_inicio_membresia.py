# Generated by Django 5.1.1 on 2024-10-24 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_usuario_trabajador'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha_inicio_membresia',
            field=models.DateField(blank=True, null=True),
        ),
    ]
