from organization.views import OrganizationViewset, PracticeViewset, ProcedureViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'organizations', OrganizationViewset, basename='organizations')
router.register(r'practices', PracticeViewset, basename='practices')
router.register(r'procedures', ProcedureViewset, basename='procedures')

urlpatterns = [
    path('', include(router.urls))
]
