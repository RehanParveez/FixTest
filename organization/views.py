from django.shortcuts import render
from rest_framework import viewsets
from organization.models import Organization, Practice, User, Procedure
from organization.serializers import OrganizationSerializers, PracticeSerializers, UserSerializers, ProcedureSerializers
from rest_framework import permissions
from organization.permissions import SuperPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from django.db import connection
from rest_framework.response import Response
from organization.permissions import SuperPermission, OrganizationPermission, PracticePermission

# Create your views here.
class OrganizationViewset(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers
    permission_classes = [permissions.IsAuthenticated, SuperPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # fields to filter
    search_fields = ['name']
    ordering_fields = ['created_at']
    filterset_fields = ['name', 'created_at']
    
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
    filterset_fields = ['location', 'organization', 'created_at']
    
    def get_permissions(self):
        if self.request.user.control == 'supadm':
            return [SuperPermission()]
        
        if self.request.user.control == 'orgadm':
            return [OrganizationPermission()]
        
        return [PracticePermission()]
    
    def get_queryset(self):
        user= self.request.user
        if user.control == 'supadm':
           return Practice.objects.all()
        if user.control == 'orgadm':
           return Practice.objects.filter(organization=user.organization)
        if user.control == 'pracadm':
            return Practice.objects.filter(id=user.practice.id)
    
    @action(detail=False, methods=['get'])
    def revenue(self, request):
       with connection.cursor() as cursor:
         cursor.execute("""
            SELECT 
                practice.id,
                practice.name,
                SUM(payment.amount) AS total_revenue
            FROM payment_payment AS payment
            JOIN patient_claim AS claim 
                ON payment.claim_id = claim.id
            JOIN patient_patient AS patient 
                ON claim.patient_id = patient.id
            JOIN organization_practice AS practice 
                ON patient.practice_id = practice.id
            GROUP BY practice.id, practice.name
            ORDER BY total_revenue DESC;
        """)
         rows = cursor.fetchall()

       data = []
       for row in rows:
          data.append({"practice_id": row[0], "practice_name": row[1], "total_revenue": row[2]})
       return Response(data)
        
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    
    # fields for filter
    ordering_fields = ['created_at']
    filterset_fields = ['organization', 'practice', 'control', 'created_at']
    
class ProcedureViewset(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    authentication_classes = [SessionAuthentication]
    
    # fields to filter
    search_fields = ['title']
    ordering_fields = ['created_at']
    filterset_fields = ['cost', 'created_at']
    
    def get_permissions(self):
        if self.request.user.control == 'supadm':
            return [SuperPermission()]
        
        if self.request.user.control == 'orgadm':
            return [OrganizationPermission()]
        return [PracticePermission()]
    
