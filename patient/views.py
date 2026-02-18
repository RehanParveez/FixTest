from django.shortcuts import render
from rest_framework import viewsets
from patient.models import Patient, Claim
from patient.serializers import PatientSerializer, ClaimSerializer

# Create your views here.
class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    def get_queryset(self):
        return Patient.objects.all()

class ClaimViewset(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    
    def get_queryset(self):
        return Claim.objects.all()
