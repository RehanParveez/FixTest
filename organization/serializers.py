from rest_framework import serializers
from organization.models import Organization, Practice, User, Procedure

class OrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'created_at']
        
class PracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = ['name', 'location', 'organization', 'created_at']
        
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone', 'created_at', 'organization', 'practice', 'dob', 'control']
        
    def create(self, validated_data):
        user=User.objects.create_user(
            name=validated_data.get('name'),
            email=validated_data.get('email'),
            phone=validated_data.get('phone'),
            created_at=validated_data.get('created_at'),
            organization=validated_data.get('organization'),
            practice=validated_data.get('practice'),
            dob=validated_data.get('dob')
        )
        return user
        
class ProcedureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['title', 'cost', 'created_at']
        
        