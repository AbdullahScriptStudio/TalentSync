from django import forms

class JobPostFormStep1(forms.Form):
    title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Job Title'}))
    company = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Company Name'}))
    country = forms.ChoiceField(choices=[('DE', 'Germany')], required=True)
    state_province = forms.ChoiceField(choices=[('Bavaria', 'Bavaria'), ('Berlin', 'Berlin')], required=True)
    city = forms.ChoiceField(choices=[('Munich', 'Munich'), ('Berlin', 'Berlin')], required=True)
    
    
    

class JobPostFormStep2(forms.Form):
    JOB_TYPES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('temporary', 'Temporary'),
    ]

    JOB_STATUS = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('paused', 'Paused'),
    ]
    
    title = forms.CharField(max_length=255, required=True, error_messages={'required': 'Job title is required!'})
    company = forms.CharField(max_length=255, required=True, error_messages={'required': 'Company name is required!'})
    country = forms.ChoiceField(choices=[('DE', 'Germany')], required=True, error_messages={'required': 'Country is required!'})
    state_province = forms.ChoiceField(choices=[('Bavaria', 'Bavaria'), ('Berlin', 'Berlin')], required=True, error_messages={'required': 'State/Province is required!'})
    city = forms.ChoiceField(choices=[('Munich', 'Munich'), ('Berlin', 'Berlin')], required=True, error_messages={'required': 'City is required!'})
    
    job_type = forms.ChoiceField(choices=JOB_TYPES, required=True, error_messages={'required': 'Job type is required!'})
    department = forms.ChoiceField(choices=[('Human Resources', 'Human Resources'), ('Engineering', 'Engineering'), ('Marketing', 'Marketing'), ('Sales', 'Sales')], required=True, error_messages={'required': 'Department is required!'})
    
    min_experience = forms.IntegerField(required=True, error_messages={'required': 'Minimum experience is required!'})
    max_experience = forms.IntegerField(required=True, error_messages={'required': 'Maximum experience is required!'})
    
    min_salary = forms.DecimalField(max_digits=10, decimal_places=2, required=True, error_messages={'required': 'Minimum salary is required!'})
    max_salary = forms.DecimalField(max_digits=10, decimal_places=2, required=True, error_messages={'required': 'Maximum salary is required!'})
    
    salary_currency = forms.ChoiceField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')], required=True, error_messages={'required': 'Salary currency is required!'})
    
    skills_required = forms.CharField(max_length=500, required=True, error_messages={'required': 'Skills are required!'})
    
    job_status = forms.ChoiceField(choices=JOB_STATUS, required=True, error_messages={'required': 'Job status is required!'})
    is_remote = forms.BooleanField(required=False)
    


class JobPostFormStep3(forms.Form):
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'w-full p-3 text-sm border rounded-xl', 'placeholder': 'Enter the job description here...'}),
        required=True,
        error_messages={'required': 'Job description is required!'}
    )