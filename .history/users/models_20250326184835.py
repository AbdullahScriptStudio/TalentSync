from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    def __str__(self):
        return self.username
