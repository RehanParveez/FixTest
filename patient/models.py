from django.db import models
from django.contrib.auth.models import User
from organization.models import Practice, Organization, Procedure

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, related_name='patients')
    created_at = models.DateTimeField(auto_now_add=True)
    
class Claim(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('complete', 'Complete'),
    )
    title = models.CharField(max_length=20)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='claims')
    procedure = models.ManyToManyField(Procedure, related_name='procedures')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)