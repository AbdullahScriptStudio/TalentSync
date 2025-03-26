from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    ]

    role = models.CharField(max_length=10, choices=USER_ROLES)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)  # Only for recruiters
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # Only for applicants

    def __str__(self):
        return self.username