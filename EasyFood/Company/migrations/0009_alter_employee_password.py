# Generated by Django 5.0 on 2024-12-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0008_employee_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
