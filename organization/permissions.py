from rest_framework import permissions
from rest_framework.permissions import BasePermission

class SuperPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.control == "supadm"
    
class OrganizationPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.control == "orgadm"
    
class PracticePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.control == 'pracadm'

class PracticePermission(permissions, BasePermission):
    def has_object_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # return request.user.is_authenticated and request.user.control == 'pracadm'