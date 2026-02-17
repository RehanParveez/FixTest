from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=20)
    employee = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizations')
    
class Practice(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='practices')
    created_at = models.DateTimeField(auto_now_add=True)
    
class Procedure(models.Model):
    title = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
