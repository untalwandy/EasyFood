# Generated by Django 5.1.4 on 2024-12-16 01:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0036_remove_contract_service_type_contract_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='Company.company', verbose_name='Cliente'),
        ),
    ]