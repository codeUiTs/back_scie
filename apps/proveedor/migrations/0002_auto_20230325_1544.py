# Generated by Django 3.2 on 2023-03-25 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='diario',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='fecha_fin',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='fecha_inicio',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
