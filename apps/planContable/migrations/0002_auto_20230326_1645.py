# Generated by Django 3.2 on 2023-03-26 22:45

import apps.base.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('facturaCliente', '0002_alter_facturacliente_cliente'),
        ('planContable', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plancontable',
            old_name='diario',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='plancontable',
            name='fecha_fin',
        ),
        migrations.RemoveField(
            model_name='plancontable',
            name='fecha_inicio',
        ),
        migrations.AddField(
            model_name='plancontable',
            name='codigo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='plancontable',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Ingreso', 'Ingreso'), ('Depreciacion', 'Depreciacion'), ('Gastos', 'Gastos'), ('Otros', 'Otros')], max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('r_object', models.JSONField(default=apps.base.models.get_r_object, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('Deudora', 'Deudora'), ('Acreedora', 'Acreedora')], max_length=255, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuentaClienteId', to='facturaCliente.cliente')),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
        migrations.AddField(
            model_name='plancontable',
            name='cuenta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuentaId', to='planContable.cuenta'),
        ),
    ]
