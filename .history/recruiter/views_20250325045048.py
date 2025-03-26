from django.shortcuts import render, redirect
from .models import JobPost
from .forms import JobPostForm  # We'll create this form next

# View to list all job posts
def job_list(request):
    job_posts = JobPost.objects.all()
    return render(request, 'recruiter/job_list.html', {'job_posts': job_posts})

# View to show details of a single job post
def job_detail(request, pk):
    job_post = JobPost.objects.get(pk=pk)
    return render(request, 'recruiter/job_detail.html', {'job_post': job_post})

# View to create a new job post
def job_create(request):
    if request.method == "POST":
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to job list after saving
    else:
        form = JobPostForm()
    return render(request, 'recruiter/job_form.html', {'form': form})
