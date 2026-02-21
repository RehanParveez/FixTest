from django.shortcuts import render
from rest_framework import viewsets
from patient.models import Patient, Claim
from patient.serializers import PatientSerializer, ClaimSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters 
from rest_framework.decorators import action
from django.db import connection
from rest_framework.response import Response
from organization.permissions import SuperPermission, OrganizationPermission, PracticePermission

# Create your views here.
class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # fields to filter
    search_fields = ['name']
    ordering_fields = ['created_at']
    
    def get_permission(self):
        if self.request.user.control == 'supadm':
            return [SuperPermission()]
        
        if self.request.user.control == 'orgadm':
            return [OrganizationPermission()]
        return [PracticePermission()]
    
    def get_queryset(self):
        user = self.request.user
        if user.control == 'supadm':
           return Patient.objects.all()
        if user.control == 'orgadm':
           return Patient.objects.filter(practice__organization=user.organization)
        if user.control == 'pracadm':
            return Patient.objects.filter(practice=user.practice)

class ClaimViewset(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # fields to filter
    search_fields = ['title']
    ordering_fields = ['created_at']
    
    def get_permissions(self):
        if self.request.user.control == 'supadm':
            return [SuperPermission()]
        
        if self.request.user.control == 'pracadm':
            return [OrganizationPermission()]
    
        return [PracticePermission()]
    
    def get_queryset(self):
        user = self.request.user
        if user.control == 'supadm':
           return Claim.objects.all()
        if user.control == 'orgadm':
            return Claim.objects.filter(patient__practice__organization=user.organization)
        if user.control == 'pracadm':
            return Claim.objects.filter(patient__practice = user.practice)
    
    @action(detail=False, methods=['get'])
    def submitted(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                   SELECT COUNT(*)
                   FROM patient_claim
                   WHERE status = 'submitted'        
            """)
            row = cursor.fetchone()
        return Response({"submitted": row[0]})
    
    @action(detail=False, methods=['get'])
    def approved(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM patient_claim
                WHERE status = 'approved'
            """)
            row = cursor.fetchone()
        return Response({'approved': row[0]})
