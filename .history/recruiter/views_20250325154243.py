from django.shortcuts import render, redirect
from .models import JobPost
#from .forms import JobPostForm  # We'll create this form next
from .forms import JobPostFormStep1, JobPostFormStep2




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
    if request.method == 'POST':
        form = JobPostFormStep1(request.POST)
        if form.is_valid():
            # Save the form data in session
            request.session['job_title'] = form.cleaned_data['title']
            request.session['company'] = form.cleaned_data['company']
            request.session['country'] = form.cleaned_data['country']
            request.session['state_province'] = form.cleaned_data['state_province']
            request.session['city'] = form.cleaned_data['city']
            
            return redirect('job_create_step2')  # Proceed to next step
    else:
        form = JobPostFormStep1()

    return render(request, 'recruiter/job_form_step1.html', {'form': form})


def job_create_step2(request):
    if request.method == 'POST':
        form = JobPostFormStep2(request.POST)
        if form.is_valid():
            # Save form data in session
            request.session['job_type'] = form.cleaned_data['job_type']
            request.session['min_experience'] = form.cleaned_data['min_experience']
            request.session['max_experience'] = form.cleaned_data['max_experience']
            request.session['min_salary'] = form.cleaned_data['min_salary']
            request.session['max_salary'] = form.cleaned_data['max_salary']
            request.session['salary_currency'] = form.cleaned_data['salary_currency']
            request.session['skills_required'] = form.cleaned_data['skills_required']
            request.session['department'] = form.cleaned_data['department']
            request.session['job_status'] = form.cleaned_data['job_status']
            request.session['is_remote'] = form.cleaned_data['is_remote']

            return redirect('job_create_step3')  # Go to next step
    else:
        form = JobPostFormStep2()

    return render(request, 'recruiter/job_form_step2.html', {'form': form})



