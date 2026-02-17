from django.contrib import admin
from patient.models import Patient, Claim

# Register your models here.
admin.site.register(Patient)
# @admin.register(Patient)
# class PatientAdmin(admin.ModelAdmin):
#     list_display = ['name', 'phone', 'practice', 'created_at']

admin.site.register(Claim)
# @admin.register(Claim)
# class ClaimAdmin(admin.ModelAdmin):
#     list_display = ['title', 'patient', 'procedure', 'status', 'created_at']
