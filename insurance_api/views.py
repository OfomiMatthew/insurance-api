
from django.shortcuts import render
from rest_framework import viewsets
from .models import InsurancePolicy, ClaimsSubmission
from .serializers import InsurancePolicySerializer, ClaimsSubmissionSerializer


class InsurancePolicyViewSet(viewsets.ModelViewSet):
    queryset = InsurancePolicy.objects.all()
    serializer_class = InsurancePolicySerializer


class ClaimsSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ClaimsSubmission.objects.all()
    serializer_class = ClaimsSubmissionSerializer
