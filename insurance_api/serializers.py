# insurance/serializers.py

from rest_framework import serializers
from .models import InsurancePolicy, ClaimsSubmission


class ClaimsSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimsSubmission
        fields = '__all__'
        depth = 1
        
    


class InsurancePolicySerializer(serializers.ModelSerializer):
    claims = ClaimsSubmissionSerializer(many=True, read_only=True)  # nested claims

    class Meta:
        model = InsurancePolicy
        fields = '__all__'
