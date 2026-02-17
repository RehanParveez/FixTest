from django.db import models
from patient.models import Claim

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    completed = models.BooleanField(default=True)
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE, related_name='payments')
    created_at = models.DateTimeField(auto_now_add=True)
    