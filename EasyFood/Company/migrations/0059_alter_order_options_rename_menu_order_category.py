# Generated by Django 5.1.4 on 2025-01-25 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0058_order_menu_alter_order_plato'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Oden', 'verbose_name_plural': 'Ordenes'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='menu',
            new_name='category',
        ),
    ]