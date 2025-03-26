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
def job_create_step1(request):
    if request.method == 'POST':
        # Step 1: Collect Job Title, Company, Country, State, City
        request.session['job_title'] = request.POST.get('title')
        request.session['company'] = request.POST.get('company')
        request.session['country'] = request.POST.get('country')
        request.session['state_province'] = request.POST.get('state_province')
        request.session['city'] = request.POST.get('city')
        
        return redirect('job_create_step2')  # Go to next step
    
    return render(request, 'recruiter/job_form_step1.html')

def job_create_step2(request):
    if request.method == 'POST':
        # Step 2: Collect Job Type, Experience, Salary, Skills, Department, Job Status, Is Remote
        request.session['job_type'] = request.POST.get('job_type')
        request.session['min_experience'] = request.POST.get('min_experience')
        request.session['max_experience'] = request.POST.get('max_experience')
        request.session['min_salary'] = request.POST.get('min_salary')
        request.session['max_salary'] = request.POST.get('max_salary')
        request.session['salary_currency'] = request.POST.get('salary_currency')
        request.session['skills_required'] = request.POST.get('skills_required')
        request.session['department'] = request.POST.get('department')
        request.session['job_status'] = request.POST.get('job_status')
        request.session['is_remote'] = request.POST.get('is_remote')
        
        return redirect('job_create_step3')  # Go to next step

    return render(request, 'recruiter/job_form_step2.html')

def job_create_step3(request):
    if request.method == 'POST':
        # Step 3: Collect Job Description
        request.session['job_description'] = request.POST.get('job_description')
        
        # Create the JobPost using data from session
        job_post = JobPost(
            title=request.session['job_title'],
            company=request.session['company'],
            country=request.session['country'],
            state_province=request.session['state_province'],
            city=request.session['city'],
            job_type=request.session['job_type'],
            min_experience=request.session['min_experience'],
            max_experience=request.session['max_experience'],
            min_salary=request.session['min_salary'],
            max_salary=request.session['max_salary'],
            salary_currency=request.session['salary_currency'],
            skills_required=request.session['skills_required'],
            department=request.session['department'],
            job_status=request.session['job_status'],
            is_remote=request.session['is_remote'],
            job_description=request.session['job_description'],
        )
        job_post.save()

        # Clear session data after saving
        request.session.flush()
        
        return redirect('job_list')  # Redirect to job list page

    return render(request, 'recruiter/addJobJobDescTwo.html')