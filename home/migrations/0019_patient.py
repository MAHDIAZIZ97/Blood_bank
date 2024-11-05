# Generated by Django 5.1 on 2024-10-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_donor_blood_group_remove_donor_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('quantity', models.PositiveIntegerField()),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_contact', models.CharField(max_length=15)),
                ('patient_address', models.TextField()),
                ('disease_name', models.CharField(blank=True, max_length=100, null=True)),
                ('hospital_name', models.CharField(blank=True, max_length=100, null=True)),
                ('hospital_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('hospital_address', models.TextField(blank=True, null=True)),
                ('hospital_city', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
