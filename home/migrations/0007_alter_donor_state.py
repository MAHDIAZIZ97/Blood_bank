# Generated by Django 5.1 on 2024-09-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_patient_address_alter_patient_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]
