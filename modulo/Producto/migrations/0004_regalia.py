# Generated by Django 5.1.1 on 2024-10-25 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0003_reserva_check_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regalia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Regalía')),
                ('foto', models.ImageField(upload_to='regalias/', verbose_name='Foto de la Regalía')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('precio', models.PositiveIntegerField(verbose_name='Precio (CLP)')),
                ('stock', models.PositiveIntegerField(verbose_name='Stock disponible')),
            ],
        ),
    ]
