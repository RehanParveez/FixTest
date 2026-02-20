from django.shortcuts import render
from rest_framework import viewsets
from patient.models import Patient, Claim
from patient.serializers import PatientSerializer, ClaimSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters 

# Create your views here.
class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # fields to filter
    search_fields = ['name']
    ordering_fields = ['created_at']
    
    def get_queryset(self):
        user = self.request.user
        if user.control == 'supadm':
           return Patient.objects.all()
        if user.control == 'orgadm':
           return Patient.objects.filter(practice_organization=user.organization)
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
    
    def get_queryset(self):
        user = self.request.user
        if user.control == 'supadm':
           return Claim.objects.all()
        if user.control == 'orgadm':
            return Claim.objects.filter(patient_practice_organization=user.organization)
        if user.control == 'pracadm':
            return Claim.objects.filter(patient_practice = user.practice)
