from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import JobPost
from django.views import View
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
class JobPostCreateView(View):
    template_name_step1 = "jobs/addJobRoleInfo.html"
    template_name_step2 = "jobs/addJobJobDescTwo.html"
    template_name_step3 = "jobs/addJobJobDescTwo.html"
    success_url = reverse_lazy('job_list')

    def get(self, request, step=1):
        """Handles GET requests for each step."""
        if step == 1:
            return render(request, self.template_name_step1)
        elif step == 2:
            return render(request, self.template_name_step2)
        elif step == 3:
            return render(request, self.template_name_step3)
        return redirect('job_list')

    def post(self, request, step=1):
        """Handles form submission step-by-step."""
        if step == 1:
            # Store step 1 data in session
            request.session['job_data'] = request.POST.dict()
            return redirect('job_create_step2')  # Move to step 2
        
        elif step == 2:
            # Merge step 2 data
            job_data = request.session.get('job_data', {})
            job_data.update(request.POST.dict())
            request.session['job_data'] = job_data
            return redirect('job_create_step3')  # Move to step 3
        
        elif step == 3:
            # Merge final step data and save the job post
            job_data = request.session.get('job_data', {})
            job_data.update(request.POST.dict())
            job = JobPost.objects.create(**job_data)
            del request.session['job_data']  # Clear session data after saving
            return redirect(self.success_url)

        return redirect('job_list')

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
