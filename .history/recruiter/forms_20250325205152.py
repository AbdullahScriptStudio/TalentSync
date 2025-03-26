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
    
    title = forms.CharField(max_length=255)
    company = forms.CharField(max_length=255)
    country = forms.ChoiceField(choices=[('DE', 'Germany')])  # Fixed to Germany
    state_province = forms.ChoiceField(choices=[('Bavaria', 'Bavaria'), ('Berlin', 'Berlin')])
    city = forms.ChoiceField(choices=[('Munich', 'Munich'), ('Berlin', 'Berlin')])
    
    job_type = forms.ChoiceField(choices=JOB_TYPES)
    department = forms.ChoiceField(choices=[('Human Resources', 'Human Resources'), 
                                             ('Engineering', 'Engineering'),
                                             ('Marketing', 'Marketing'),
                                             ('Sales', 'Sales')])
    min_experience = forms.IntegerField()
    max_experience = forms.IntegerField()
    min_salary = forms.DecimalField(max_digits=10, decimal_places=2)
    max_salary = forms.DecimalField(max_digits=10, decimal_places=2)
    salary_currency = forms.ChoiceField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')])
    
    skills_required = forms.CharField(max_length=500, required=False)
    
    job_status = forms.ChoiceField(choices=JOB_STATUS)
    is_remote = forms.BooleanField(required=False)

    


class JobPostFormStep3(forms.Form):
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'w-full p-3 text-sm border rounded-xl', 'placeholder': 'Enter the job description here...'}),
        required=True,
        error_messages={'required': 'Job description is required!'}
    )