from rest_framework.permissions import BasePermission

class SuperPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.control == "supadm"
    
    def has_object_permission(self, request, view, object):
        return True
    
class OrganizationPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.control == "orgadm"
    
    def has_object_permission(self, request, view, obj):
        organization_user = request.user.organization
        
        if hasattr(obj, 'organization'):
            return obj.organization == organization_user
        
        if hasattr(obj, 'practice'):
            return obj.practice_organization == organization_user
        
        if hasattr(obj, 'patient'):
            return obj.patient.practice.organization == organization_user
        
        if hasattr(obj, 'claim'):
            return obj.claim.patient.practice.organization == organization_user
        return False
    
class PracticePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.control == 'pracadm'
    
    def has_object_permission(self, request, view, obj):
        practice_user = request.user.practice
        
        if hasattr(obj, 'practice'):
            return obj.practice == practice_user
        
        if hasattr(obj, 'patient'):
            return obj.patient.practice == practice_user
        
        if hasattr(obj, 'claim'):
            return obj.claim.patient.practice == practice_user
        return False

