from django.contrib import admin
from .models import ClaimsSubmission, InsurancePolicy

# Register your models here.
admin.site.register(ClaimsSubmission)
admin.site.register(InsurancePolicy)
