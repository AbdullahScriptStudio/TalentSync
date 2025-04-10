# Generated by Django 5.1.7 on 2025-03-26 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('country', models.CharField(default='DE', max_length=2)),
                ('state_province', models.CharField(choices=[('Baden-Württemberg', 'Baden-Württemberg'), ('Bavaria', 'Bavaria'), ('Berlin', 'Berlin'), ('Brandenburg', 'Brandenburg'), ('Bremen', 'Bremen'), ('Hamburg', 'Hamburg'), ('Hesse', 'Hesse'), ('Lower Saxony', 'Lower Saxony'), ('Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern'), ('North Rhine-Westphalia', 'North Rhine-Westphalia'), ('Rhineland-Palatinate', 'Rhineland-Palatinate'), ('Saarland', 'Saarland'), ('Saxony', 'Saxony'), ('Saxony-Anhalt', 'Saxony-Anhalt'), ('Schleswig-Holstein', 'Schleswig-Holstein'), ('Thuringia', 'Thuringia')], max_length=100)),
                ('city', models.CharField(choices=[('Berlin', 'Berlin'), ('Munich', 'Munich'), ('Hamburg', 'Hamburg'), ('Cologne', 'Cologne'), ('Frankfurt', 'Frankfurt'), ('Stuttgart', 'Stuttgart'), ('Düsseldorf', 'Düsseldorf'), ('Dortmund', 'Dortmund'), ('Essen', 'Essen'), ('Leipzig', 'Leipzig')], max_length=100)),
                ('company', models.CharField(max_length=255)),
                ('job_type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contract', 'Contract'), ('freelance', 'Freelance'), ('temporary', 'Temporary')], max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('min_experience', models.PositiveIntegerField()),
                ('max_experience', models.PositiveIntegerField()),
                ('min_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_currency', models.CharField(choices=[('EUR', 'Euro (EUR)'), ('USD', 'United States Dollar (USD)'), ('GBP', 'British Pound (GBP)'), ('AUD', 'Australian Dollar (AUD)'), ('CAD', 'Canadian Dollar (CAD)')], default='EUR', max_length=3)),
                ('skills_required', models.CharField(max_length=500)),
                ('job_description', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('paused', 'Paused')], default='open', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=255)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.TextField(blank=True)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.jobpost')),
            ],
        ),
    ]
