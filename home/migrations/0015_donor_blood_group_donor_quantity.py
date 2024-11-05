# Generated by Django 5.1 on 2024-10-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_donor'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='blood_group',
            field=models.CharField(default='Unknown', max_length=10),
        ),
        migrations.AddField(
            model_name='donor',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]