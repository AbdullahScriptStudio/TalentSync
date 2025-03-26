from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobPost(models.Model):
    JOB_TYPES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('temporary', 'Temporary'),
    ]

    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state_province = models.CharField(max_length=100, blank=True)  # Optional
    city = models.CharField(max_length=100, blank=True)  # Optional
    company = models.CharField(max_length=255)
    job_type = models.CharField(choices=JOB_TYPES, max_length=50)
    department = models.CharField(max_length=100)
    min_experience = models.PositiveIntegerField()
    max_experience = models.PositiveIntegerField()
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_currency = models.CharField(max_length=10, default='USD')
    skills_required = models.ManyToManyField(Skill, blank=True)  # Optional, can have multiple skills
    job_description = models.TextField()
    status = models.CharField(choices=[('active', 'Active'), ('closed', 'Closed'), ('on_hold', 'On Hold')], max_length=20, default='active')
    application_deadline = models.DateField(null=True, blank=True)
    is_remote = models.BooleanField(default=False)
    company_description = models.TextField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
