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
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users')
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, related_name='users')
    dob = models.DateField()
    
    def __str__(self):
        return self.name
    
class Procedure(models.Model):
    title = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
