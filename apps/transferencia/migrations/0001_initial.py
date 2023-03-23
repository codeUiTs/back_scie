# Generated by Django 3.2 on 2023-03-23 17:43

import apps.base.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('r_object', models.JSONField(default=apps.base.models.get_r_object, null=True)),
                ('diario', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('fecha_fin', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Transferencia',
                'verbose_name_plural': 'Transferencias',
            },
        ),
    ]
