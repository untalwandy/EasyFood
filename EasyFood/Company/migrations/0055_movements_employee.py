# Generated by Django 5.1.4 on 2025-01-06 02:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0054_movements'),
    ]

    operations = [
        migrations.AddField(
            model_name='movements',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='Company.employee', verbose_name='Empleado'),
        ),
    ]