from django.contrib import admin
from payment.models import Payment

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['amount', 'completed', 'claim', 'created_at']
