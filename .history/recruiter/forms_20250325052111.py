from django import forms
from .models import JobPost

class JobPostFormStep1(forms.Form):
    title = forms.CharField(max_length=255)
    company = forms.CharField(max_length=255)
    country = forms.ChoiceField(choices=[('DE', 'Germany')])  # Fixed to Germany
    state_province = forms.ChoiceField(choices=[
        ('Bavaria', 'Bavaria'),
        ('Berlin', 'Berlin'),
        # Add more states
    ])
    city = forms.ChoiceField(choices=[
        ('Munich', 'Munich'),
        ('Berlin', 'Berlin'),
        # Add more cities
    ])
