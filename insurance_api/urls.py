# insurance/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InsurancePolicyViewSet, ClaimsSubmissionViewSet,SupportingDocumentUploadView

router = DefaultRouter()
router.register(r'policies', InsurancePolicyViewSet)
router.register(r'claims', ClaimsSubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('claims/upload/', SupportingDocumentUploadView.as_view(), name='upload-supporting-doc'),
]
