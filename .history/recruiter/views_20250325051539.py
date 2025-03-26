from django.shortcuts import render, redirect
from .models import JobPost
#from .forms import JobPostForm  # We'll create this form next
from .forms import JobPostFormStep1




# View to list all job posts
def job_list(request):
    job_posts = JobPost.objects.all()
    return render(request, 'recruiter/job_list.html', {'job_posts': job_posts})

# View to show details of a single job post
def job_detail(request, pk):
    job_post = JobPost.objects.get(pk=pk)
    return render(request, 'recruiter/job_detail.html', {'job_post': job_post})

# View to create a new job post
def job_create_step1(request):
    form = JobPostFormStep1
    if request.method == 'POST':
        form = JobPostFormStep1(request.POST)
        if form.is_valid():
            # Save the data to the session
            request.session['job_title'] = form.cleaned_data['title']
            request.session['company'] = form.cleaned_data['company']
            request.session['country'] = form.cleaned_data['country']
            request.session['state_province'] = form.cleaned_data['state_province']
            request.session['city'] = form.cleaned_data['city']
            
            return redirect('job_create_step2')  # Proceed to next step
    else:
        form = JobPostFormStep1()
        
    return render(request, 'recruiter/job_form_step1.html')
