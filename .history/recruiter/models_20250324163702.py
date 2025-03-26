from django.db import models

class JobPost(models.Model):
    # Define a fixed country (Germany)
    COUNTRY = 'DE'
    
    JOB_TYPES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('temporary', 'Temporary'),
    ]

    # Define German states (Bundesländer)
    GERMAN_STATES = [
        ('Baden-Württemberg', 'Baden-Württemberg'),
        ('Bavaria', 'Bavaria'),
        ('Berlin', 'Berlin'),
        ('Brandenburg', 'Brandenburg'),
        ('Bremen', 'Bremen'),
        ('Hamburg', 'Hamburg'),
        ('Hesse', 'Hesse'),
        ('Lower Saxony', 'Lower Saxony'),
        ('Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern'),
        ('North Rhine-Westphalia', 'North Rhine-Westphalia'),
        ('Rhineland-Palatinate', 'Rhineland-Palatinate'),
        ('Saarland', 'Saarland'),
        ('Saxony', 'Saxony'),
        ('Saxony-Anhalt', 'Saxony-Anhalt'),
        ('Schleswig-Holstein', 'Schleswig-Holstein'),
        ('Thuringia', 'Thuringia'),
    ]
    
    # Define major cities for each state (optional if needed)
    GERMAN_CITIES = [
        ('Berlin', 'Berlin'),
        ('Munich', 'Munich'),
        ('Hamburg', 'Hamburg'),
        ('Cologne', 'Cologne'),
        ('Frankfurt', 'Frankfurt'),
        ('Stuttgart', 'Stuttgart'),
        ('Düsseldorf', 'Düsseldorf'),
        ('Dortmund', 'Dortmund'),
        ('Essen', 'Essen'),
        ('Leipzig', 'Leipzig'),
    ]
    
    # Define available salary currencies
    CURRENCY_CHOICES = [
        ('EUR', 'Euro (EUR)'),
        ('USD', 'United States Dollar (USD)'),
        ('GBP', 'British Pound (GBP)'),
        ('AUD', 'Australian Dollar (AUD)'),
        ('CAD', 'Canadian Dollar (CAD)'),
    ]
    
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=2, default=COUNTRY)  # Fixed to 'DE' for Germany
    state_province = models.CharField(choices=GERMAN_STATES, max_length=100)  # Dropdown with German states
    city = models.CharField(choices=GERMAN_CITIES, max_length=100)  # Dropdown with German cities
    company = models.CharField(max_length=255)
    job_type = models.CharField(choices=JOB_TYPES, max_length=50)
    department = models.CharField(max_length=100)
    min_experience = models.PositiveIntegerField()
    max_experience = models.PositiveIntegerField()
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, default='EUR')  # Dropdown for currency
    skills_required = models.CharField(max_length=500)  # Multiple keywords as comma-separated values
    job_description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Application(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)  # Optional cover letter field
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[('received', 'Received'), ('under_review', 'Under Review'), ('shortlisted', 'Shortlisted'), ('rejected', 'Rejected')], max_length=20, default='received')

    def __str__(self):
        return f"Application from {self.applicant_name} for {self.job_post.title}"