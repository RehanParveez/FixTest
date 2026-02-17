from rest_framework import serializers
from patient.models import Patient, Claim

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'phone', 'practice', 'created_at']
        
class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = ['title', 'patient', 'procedure', 'status', 'created_at']