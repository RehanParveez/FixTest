from django.db import models
from organization.models import Practice, Procedure

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, related_name='patients')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Claim(models.Model):
    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
    )
    title = models.CharField(max_length=20)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='claims')
    procedure = models.ManyToManyField(Procedure, related_name='procedures')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    