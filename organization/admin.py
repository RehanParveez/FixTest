from django.contrib import admin
from organization.models import Organization, Practice, User, Procedure
# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    
@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'organization', 'created_at']
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone', 'created_at', 'organization', 'practice', 'dob', 'control']
    
@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ['title', 'cost', 'created_at']
