# Generated by Django 5.1.4 on 2024-12-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0031_alter_plato_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]
