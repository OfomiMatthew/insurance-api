# models.py
from django.db import models



class InsuranceClaim(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    policy_number = models.CharField(max_length=100)
    claim_type = models.CharField(max_length=30)
    incident_date = models.DateField()
    description = models.TextField()
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    supporting_document = models.FileField(upload_to='claims/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.claim_type} - {self.policy_number}"
