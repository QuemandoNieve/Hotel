# Generated by Django 5.1 on 2024-12-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0024_reservaregalia_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservaregalia',
            name='usada',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
