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
    
    salary_currency_choices = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
    ]

    job_type = forms.ChoiceField(choices=JOB_TYPES, required=True)
    department = forms.CharField(max_length=100, required=True)
    min_experience = forms.IntegerField(required=True, min_value=0)
    max_experience = forms.IntegerField(required=True, min_value=0)
    min_salary = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    max_salary = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    salary_currency = forms.ChoiceField(choices=salary_currency_choices, required=True)
    skills_required = forms.CharField(max_length=500, required=True)

    def clean(self):
        cleaned_data = super().clean()
        
        # Validate that min_experience is less than or equal to max_experience
        min_exp = cleaned_data.get('min_experience')
        max_exp = cleaned_data.get('max_experience')
        
        if min_exp and max_exp and min_exp > max_exp:
            raise forms.ValidationError("Minimum experience must be less than or equal to maximum experience.")
        
        # Validate that min_salary is less than or equal to max_salary
        min_sal = cleaned_data.get('min_salary')
        max_sal = cleaned_data.get('max_salary')
        
        if min_sal and max_sal and min_sal > max_sal:
            raise forms.ValidationError("Minimum salary must be less than or equal to maximum salary.")
        
        return cleaned_data
    


class JobPostFormStep3(forms.Form):
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'w-full p-3 text-sm border rounded-xl', 'placeholder': 'Enter the job description here...'}),
        required=True,
        error_messages={'required': 'Job description is required!'}
    )