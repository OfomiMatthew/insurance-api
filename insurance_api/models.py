from django.db import models

class InsurancePolicy(models.Model):
  COVERAGE_CHOICES = [
        ('health', 'Health'),
        ('work', 'Work'),
        ('life', 'Life'),
    ]
  policy_number = models.CharField(primary_key=True)
  coverage_type = models.CharField(max_length=10, choices=COVERAGE_CHOICES)
  
  def __str__(self):
        return f"{self.policy_number} - {self.coverage_type.capitalize()}"
  

class ClaimsSubmission(models.Model):
  # insurance_policy = models.ForeignKey(InsurancePolicy,on_delete=models.CASCADE,related_name='claims')
  claim_number = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  claim_type = models.CharField(
        max_length=50,
        
    )
  supporting_documents = models.FileField(upload_to='claims/docs/', null=True, blank=True)
  date_submitted = models.DateField(auto_now_add=True)
  

  def __str__(self):
        return f"Claim {self.claim_number} for Policy {self.insurance_policy.policy_number}"

