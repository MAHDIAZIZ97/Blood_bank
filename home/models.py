from django.db import models
# from django.contrib.auth.models import User


class Product(models.Model):
    blood_id=models.AutoField
    blood_name = models.CharField(max_length=50)
    blood_stock = models.PositiveIntegerField()
    blood_image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.blood_name


# Donor form

class Donor(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=3, blank=True, null=True, choices=BLOOD_GROUP_CHOICES)
    donor_name = models.CharField(max_length=100)
    donor_contact = models.CharField(max_length=15)
    donor_address = models.CharField(max_length=255)
    donor_disease = models.CharField(max_length=255)
    donor_city = models.CharField(max_length=100)
    donor_zip_code = models.CharField(max_length=10)
    donor_state = models.CharField(max_length=50)

    def __str__(self):
        return self.donor_name


# patient form

class Patient(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    quantity = models.PositiveIntegerField()
    patient_name = models.CharField(max_length=100)
    patient_contact = models.CharField(max_length=15)
    patient_address = models.TextField()

    
    disease_name = models.CharField(max_length=100, blank=True, null=True) 
    hospital_name = models.CharField(max_length=100, blank=True, null=True)  
    hospital_contact = models.CharField(max_length=15, blank=True, null=True)
    hospital_address = models.TextField(blank=True, null=True)
    hospital_city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    blood_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Patient {self.patient_name} - {self.blood_group}"



