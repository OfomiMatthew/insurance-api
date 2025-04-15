from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import InsuranceClaimForm

def submit_claim(request):
    if request.method == 'POST':
        form = InsuranceClaimForm(request.POST, request.FILES)
        if form.is_valid():
            claim = form.save()

            # Create a key-value email body
            data = form.cleaned_data
            email_body = '\n'.join([f"{field.label}: {data[field.name]}" for field in form])

            # Prepare the email
            email = EmailMessage(
                subject='New Insurance Claim Submission',
                body=email_body,
                from_email='mofomi@saconsulting.ai',
                to=['mofomi@saconsulting.ai'],  # Replace with desired recipient
            )

            # Attach uploaded document safely
            uploaded_file = request.FILES.get('supporting_document')
            if uploaded_file:
                email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)

            email.send()
            messages.success(request, "✅ Your insurance claim has been received. We'll contact you shortly.")
            return redirect('submit-claim')  # Or a thank-you page
    else:
        form = InsuranceClaimForm()

    return render(request, 'submit_claim.html', {'form': form})
