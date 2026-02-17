from rest_framework import serializers
from organization.models import Organization, Practice, Procedure
from django.contrib.auth.models import User

class OrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'employee', 'created_at']
        
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']

class PracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = ['name', 'location', 'organization', 'created_at']
        
class ProcedureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['title', 'cost', 'created_at']
        
        
        