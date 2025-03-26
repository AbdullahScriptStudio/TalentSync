from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)

    def __str__(self):
        return self.username
