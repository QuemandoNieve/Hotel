# Generated by Django 5.0.4 on 2024-10-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0003_usuario_fecha_inicio_membresia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='imagen_mascota',
            field=models.ImageField(blank=True, null=True, upload_to='mascotas/'),
        ),
    ]
