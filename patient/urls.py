from rest_framework.routers import DefaultRouter
from patient.views import PatientViewset, ClaimViewset
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'Patients', PatientViewset, basename='patients')
router.register(r'Claims', ClaimViewset, basename='claims')

urlpatterns = [
    path('', include(router.urls)),
    path('tokenobtain/', TokenObtainPairView.as_view()),
    path('tokenrefresh/', TokenRefreshView.as_view()),
]

