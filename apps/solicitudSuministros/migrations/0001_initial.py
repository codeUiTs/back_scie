# Generated by Django 3.2 on 2023-02-23 15:56

import apps.base.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('r_object', models.JSONField(default=apps.base.models.get_r_object, null=True)),
                ('producto_solicitado', models.CharField(max_length=255, null=True)),
                ('producto_entregado', models.CharField(max_length=255, null=True)),
                ('cantidad_solicitada', models.CharField(max_length=255)),
                ('cantidad', models.CharField(max_length=255)),
                ('cantidad_real', models.CharField(max_length=255, null=True)),
                ('medida', models.CharField(max_length=255, null=True)),
                ('partida', models.CharField(max_length=255, null=True)),
                ('estado', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Solicitud de Suministro',
                'verbose_name_plural': 'Solicitud de Suministros',
            },
        ),
    ]