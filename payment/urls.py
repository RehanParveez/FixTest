from rest_framework.routers import DefaultRouter
from payment.views import PaymentViewset
from django.urls import path, include

router = DefaultRouter()
router.register(r'Payments', PaymentViewset, basename='payments')

urlpatterns = [
    path('', include(router.urls))
]

