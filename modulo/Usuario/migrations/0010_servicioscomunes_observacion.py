# Generated by Django 5.0.4 on 2024-10-31 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0009_servicioscomunes_reserva_alter_servicioscomunes_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicioscomunes',
            name='observacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
