from django.contrib import admin
from organization.models import Organization, Practice, Procedure
# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee', 'created_at', 'user']
    
@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'organization', 'created_at']
    
@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ['title', 'cost', 'created_at']
