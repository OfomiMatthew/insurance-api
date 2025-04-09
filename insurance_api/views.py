from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from .models import InsurancePolicy, ClaimsSubmission
from .serializers import InsurancePolicySerializer, ClaimsSubmissionSerializer,SupportingDocumentUploadSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class InsurancePolicyViewSet(viewsets.ModelViewSet):
    queryset = InsurancePolicy.objects.all()
    serializer_class = InsurancePolicySerializer


class ClaimsSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ClaimsSubmission.objects.all()
    serializer_class = ClaimsSubmissionSerializer
    
    @action(detail=True, methods=['post'], parser_classes=[MultiPartParser, FormParser])
    def upload(self, request, pk=None):
        claim = self.get_object()
        serializer = SupportingDocumentUploadSerializer(claim, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Document uploaded successfully'})
        return Response(serializer.errors, status=400)
    
class SupportingDocumentUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
   
    def post(self, request, *args, **kwargs):
        claim_id = request.data.get('claim_id')  # You pass this in your form data
        try:
            claim = ClaimsSubmission.objects.get(id=claim_id)
        except ClaimsSubmission.DoesNotExist:
            return Response({'error': 'Claim not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SupportingDocumentUploadSerializer(claim, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Document uploaded successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
