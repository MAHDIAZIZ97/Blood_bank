# Generated by Django 5.1 on 2024-10-27 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_donor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='quantity',
        ),
    ]