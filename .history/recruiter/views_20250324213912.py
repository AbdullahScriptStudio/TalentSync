from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import JobPost

# List all job posts
class JobPostListView(ListView):
    model = JobPost
    template_name = "jobs/job_list.html"  # Create this template
    context_object_name = "jobs"

# Show details of a job post
class JobPostDetailView(DetailView):
    model = JobPost
    template_name = "jobs/job_detail.html"  # Create this template
    context_object_name = "job"

# Create a new job post
class JobPostCreateView(CreateView):
    model = JobPost
    template_name = "jobs/job_form.html"  # Create this template
    fields = ['title', 'state_province', 'city', 'company', 'job_type', 'department', 'min_experience', 
              'max_experience', 'min_salary', 'max_salary', 'salary_currency', 'skills_required', 
              'job_description', 'status']
    success_url = reverse_lazy('job_list')  # Redirect after success

# Update an existing job post
class JobPostUpdateView(UpdateView):
    model = JobPost
    template_name = "jobs/job_form.html"  # Same form template as CreateView
    fields = ['title', 'state_province', 'city', 'company', 'job_type', 'department', 'min_experience', 
              'max_experience', 'min_salary', 'max_salary', 'salary_currency', 'skills_required', 
              'job_description', 'status']
    success_url = reverse_lazy('job_list')  # Redirect after success

# Delete a job post
class JobPostDeleteView(DeleteView):
    model = JobPost
    template_name = "jobs/job_confirm_delete.html"  # Create this template
    success_url = reverse_lazy('job_list')  # Redirect after success
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import JobPost

# List all job posts
class JobPostListView(ListView):
    model = JobPost
    template_name = "jobs/job_list.html"  # Create this template
    context_object_name = "jobs"

# Show details of a job post
class JobPostDetailView(DetailView):
    model = JobPost
    template_name = "jobs/job_detail.html"  # Create this template
    context_object_name = "job"

# Create a new job post
class JobPostCreateView(CreateView):
    model = JobPost
    template_name = "jobs/job_form.html"  # Create this template
    fields = ['title', 'state_province', 'city', 'company', 'job_type', 'department', 'min_experience', 
              'max_experience', 'min_salary', 'max_salary', 'salary_currency', 'skills_required', 
              'job_description', 'status']
    success_url = reverse_lazy('job_list')  # Redirect after success

# Update an existing job post
class JobPostUpdateView(UpdateView):
    model = JobPost
    template_name = "jobs/job_form.html"  # Same form template as CreateView
    fields = ['title', 'state_province', 'city', 'company', 'job_type', 'department', 'min_experience', 
              'max_experience', 'min_salary', 'max_salary', 'salary_currency', 'skills_required', 
              'job_description', 'status']
    success_url = reverse_lazy('job_list')  # Redirect after success

# Delete a job post
class JobPostDeleteView(DeleteView):
    model = JobPost
    template_name = "jobs/job_confirm_delete.html"  # Create this template
    success_url = reverse_lazy('job_list')  # Redirect after success
