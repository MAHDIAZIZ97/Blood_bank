# Generated by Django 5.1 on 2024-10-03 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='blood_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='blood_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='blood_stock',
        ),
    ]
