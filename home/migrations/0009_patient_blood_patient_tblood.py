# Generated by Django 5.1 on 2024-09-21 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_patient_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='blood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='tblood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
