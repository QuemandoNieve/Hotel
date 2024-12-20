# Generated by Django 5.0.4 on 2024-10-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0010_servicioscomunes_observacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicioscomunes',
            name='comio_evidencia',
            field=models.ImageField(blank=True, null=True, upload_to='evidencias/comio/'),
        ),
        migrations.AddField(
            model_name='servicioscomunes',
            name='entretencion_evidencia',
            field=models.ImageField(blank=True, null=True, upload_to='evidencias/entretencion/'),
        ),
        migrations.AddField(
            model_name='servicioscomunes',
            name='medicamentos_evidencia',
            field=models.ImageField(blank=True, null=True, upload_to='evidencias/medicamentos/'),
        ),
        migrations.AddField(
            model_name='servicioscomunes',
            name='paseo_evidencia',
            field=models.ImageField(blank=True, null=True, upload_to='evidencias/paseo/'),
        ),
    ]
