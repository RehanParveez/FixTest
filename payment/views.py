from django.shortcuts import render
from rest_framework import viewsets
from payment.models import Payment
from payment.serializers import PaymentSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from django.db import connection
from rest_framework.response import Response
from django.db import transaction
from organization.permissions import SuperPermission, OrganizationPermission, PracticePermission

# Create your views here.
class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # fields to filter
    search_fields = ['amount']
    ordering_fields = ['created_at']
    
    def get_permissions(self):
        if self.request.user.control == 'supadm':
            return [SuperPermission()]
        
        if self.request.user.control == 'orgadm':
            return [OrganizationPermission()]
        
        return [PracticePermission()]
    
    def get_queryset(self):
        user = self.request.user
        if user.control == 'supadm':
           return Payment.objects.all()
        if user.control == 'orgadm':
            return Payment.objects.filter(claim__patient__practice__organization=user.organization)
        if user.control == 'pracadm':
            return Payment.objects.filter(claim__patient__practice=user.practice)
    
    @action(detail=False, methods=['get'])
    def paid(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT SUM(amount) 
            FROM payment_payment
            WHERE completed = 1;              
            """)
            row = cursor.fetchone()
        return Response({'paid':row[0]})
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        return Response(serializer.data)
            

