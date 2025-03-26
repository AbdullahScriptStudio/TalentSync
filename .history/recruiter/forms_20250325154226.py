from django import forms

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



class JobPostFormStep2(forms.Form):
    JOB_TYPES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('temporary', 'Temporary'),
    ]
    
    SALARY_CURRENCY_CHOICES = [
        ('EUR', 'Euro (EUR)'),
        ('USD', 'United States Dollar (USD)'),
        ('GBP', 'British Pound (GBP)'),
        ('AUD', 'Australian Dollar (AUD)'),
        ('CAD', 'Canadian Dollar (CAD)'),
    ]

    job_type = forms.ChoiceField(choices=JOB_TYPES)
    min_experience = forms.IntegerField(min_value=0)
    max_experience = forms.IntegerField(min_value=0)
    min_salary = forms.DecimalField(max_digits=10, decimal_places=2)
    max_salary = forms.DecimalField(max_digits=10, decimal_places=2)
    salary_currency = forms.ChoiceField(choices=SALARY_CURRENCY_CHOICES)
    skills_required = forms.CharField(max_length=500)  # Comma separated skills
    department = forms.CharField(max_length=100)
    job_status = forms.ChoiceField(choices=[('open', 'Open'), ('closed', 'Closed'), ('paused', 'Paused')])
    is_remote = forms.BooleanField(required=False)
    


class JobPostFormStep3(forms.Form):
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'w-full p-3 text-sm border rounded-xl', 'placeholder': 'Enter the job description here...'}),
        required=True
    )