from django.shortcuts import render, redirect
from .models import JobPost
#from .forms import JobPostForm  # We'll create this form next
from .forms import JobPostFormStep1, JobPostFormStep2, JobPostFormStep3




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
            # Save form data in session
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
            # Collect data from the form
            job_status = form.cleaned_data['job_status']
            skills_required = form.cleaned_data['skills_required']
            
            # Save this data into the session to pass to the next step
            request.session['job_status'] = job_status
            request.session['skills_required'] = skills_required
            
            # Save other fields into the session if needed
            # Proceed to Step 3
            return redirect('job_create_step3')
        else:
            # If form is not valid, stay on step 2 and display errors
            return render(request, 'recruiter/job_form_step2.html', {'form': form})
    else:
        form = JobPostFormStep2()

    return render(request, 'recruiter/job_form_step2.html', {'form': form})