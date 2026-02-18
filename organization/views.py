from django.shortcuts import render
from rest_framework import viewsets
from organization.models import Organization, Practice, Procedure
from organization.serializers import OrganizationSerializers, PracticeSerializers, ProcedureSerializers

# Create your views here.
class OrganizationViewset(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers
    
    def get_queryset(self):
        return Organization.objects.all()

class PracticeViewset(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializers
    
    def get_queryset(self):
        return Practice.objects.all() 
    
class ProcedureViewset(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializers
    
    def get_queryset(self):
        return Procedure.objects.all()
    
    
    
