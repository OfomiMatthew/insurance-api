# forms.py
from django import forms
from .models import InsuranceClaim

class InsuranceClaimForm(forms.ModelForm):
    class Meta:
        model = InsuranceClaim
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': '+234...'}),
            'policy_number': forms.TextInput(attrs={'class': 'input'}),
            'claim_type': forms.TextInput(attrs={'class': 'input'}),
            'incident_date': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Brief description of the incident'}),
            'claim_amount': forms.NumberInput(attrs={'class': 'input'}),
        }
