# Generated by Django 5.1.4 on 2025-01-06 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0053_contract_firma_company_contract_firma_resturant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_move', models.CharField(choices=[('ingreso', 'Ingreso'), ('gasto', 'Gasto'), ('acciones', 'Acciones')], max_length=10, verbose_name='Tipo de Movimiento')),
                ('mount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Monto')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Movimiento')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='Company.company', verbose_name='Empresa')),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='Company.restaurant', verbose_name='Restaurante')),
            ],
        ),
    ]