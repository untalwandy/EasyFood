# Generated by Django 5.1.4 on 2024-12-13 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0028_menu_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/service/'),
        ),
    ]