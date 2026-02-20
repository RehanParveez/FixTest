from django.shortcuts import render
from rest_framework import viewsets
from organization.models import Organization, Practice, User, Procedure
from organization.serializers import OrganizationSerializers, PracticeSerializers, UserSerializers, ProcedureSerializers
from rest_framework import permissions
from organization.permissions import SuperPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication

# Create your views here.
class OrganizationViewset(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers
    permission_classes = [permissions.IsAuthenticated, SuperPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # fields to filter
    search_fields = ['name']
    ordering_fields = ['created_at']
    
    def get_queryset(self):
        return Organization.objects.all()
    
class PracticeViewset(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # fields to filter
    search_fields = ['name']
    ordering_fields = ['created_at']
    
    def get_queryset(self):
        user= self.request.user
        if user.control == 'supadm':
           return Practice.objects.all()
        if user.control == 'orgadm':
           return Practice.objects.filter(organization=user.organization)
        if user.control == 'pracadm':
            return Practice.objects.filter(id=user.practice.id)
        
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    
    # fields for filter
    ordering_fields = ['created_at']
    
class ProcedureViewset(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    authentication_classes = [SessionAuthentication]
    
    # fields to filter
    search_fields = ['title']
    ordering_fields = ['created_at']
    
    def get_queryset(self):
        user = self.request.user
        if user.control == 'supadm':
            return Procedure.objects.all()
        if user.control == 'orgadm':
            return Procedure.objects.filter(claim_patient_practice_organization=user.organization)
        if user.control == 'pracadm':
            return Procedure.objects.filter(claim_patient_practice = user.practice)
    
