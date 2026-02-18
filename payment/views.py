from django.shortcuts import render
from rest_framework import viewsets
from payment.models import Payment
from payment.serializers import PaymentSerializer

# Create your views here.
class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def get_queryset(self):
        return Payment.objects.all()
    

