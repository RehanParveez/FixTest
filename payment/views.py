from django.shortcuts import render
from rest_framework import viewsets
from payment.models import Payment
from payment.serializers import PaymentSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # fields to filter
    search_fields = ['amount']
    ordering_fields = ['created_at']
    
    def get_queryset(self):
        user = self.request.user
        if user.control == 'supadm':
           return Payment.objects.all()
        if user.control == 'orgadm':
            return Payment.objects.filter(claim_patient_practice_organization=user.organization)
        if user.control == 'pracadm':
            return Payment.objects.filter(claim_patient_practice=user.practice)
            

