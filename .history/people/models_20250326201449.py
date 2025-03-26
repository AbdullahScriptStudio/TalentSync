from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='applicant')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username
