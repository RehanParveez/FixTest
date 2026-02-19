from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Practice(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='practices')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    CONTROL_CHOICES = (
        ('supadm', 'SupAdm'),
        ('orgadm', 'OrgAdm'),
        ('pracadm', 'PracAdm')
    )
    phone = models.CharField(max_length=20 ,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, related_name='users')
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, null=True, related_name='users')
    dob = models.DateField(null=True)
    control = models.CharField(max_length=20, choices=CONTROL_CHOICES, default='pracadm')
    
    def __str__(self):
        return self.username
    
class Procedure(models.Model):
    title = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
