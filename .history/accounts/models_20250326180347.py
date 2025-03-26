from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='applicant')
    company_name = models.CharField(max_length=255, blank=True, null=True)  # Recruiters only
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # Applicants only

    def is_recruiter(self):
        return self.user_type == 'recruiter'

    def is_applicant(self):
        return self.user_type == 'applicant'

    def __str__(self):
        return self.username
