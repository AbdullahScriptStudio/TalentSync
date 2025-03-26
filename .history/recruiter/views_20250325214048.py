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






def job_create_step3(request):
    if request.method == 'POST':
        form = JobPostFormStep3(request.POST)
        if form.is_valid():
            # Collect data from session (Step 1, Step 2, and Step 3)
            title = request.session.get('job_title', '')
            company = request.session.get('company', '')
            country = request.session.get('country', 'DE')
            state_province = request.session.get('state_province', 'Bavaria')
            city = request.session.get('city', 'Munich')
            job_type = request.session.get('job_type', 'full_time')
            department = request.session.get('department', '')
            min_experience = request.session.get('min_experience', 0)
            max_experience = request.session.get('max_experience', 0)
            min_salary = request.session.get('min_salary', 0.0)
            max_salary = request.session.get('max_salary', 0.0)
            salary_currency = request.session.get('salary_currency', 'EUR')
            skills_required = request.session.get('skills_required', '')
            job_description = form.cleaned_data['job_description']
            job_status = request.session.get('job_status', 'open')  # This was collected in Step 2

            # Save the data to the database
            job_post = JobPost(
                title=title,
                company=company,
                country=country,
                state_province=state_province,
                city=city,
                job_type=job_type,
                department=department,
                min_experience=min_experience,
                max_experience=max_experience,
                min_salary=min_salary,
                max_salary=max_salary,
                salary_currency=salary_currency,
                skills_required=skills_required,
                job_description=job_description,
                status=job_status,
            )
            job_post.save()

            # Optionally, clear session data if not needed anymore
            request.session.flush()

            # Redirect to a summary or success page
            return redirect('job_create_summary')  # This is a hypothetical summary page
    else:
        form = JobPostFormStep3()

    return render(request, 'recruiter/job_form_step3.html', {'form': form})


def job_create_step3(request):
    if request.method == 'POST':
        form = JobPostFormStep3(request.POST)
        if form.is_valid():
            # Collect data from session (Step 1, Step 2, and Step 3)
            title = request.session.get('job_title', '')
            company = request.session.get('company', '')
            country = request.session.get('country', 'DE')
            state_province = request.session.get('state_province', 'Bavaria')
            city = request.session.get('city', 'Munich')
            job_type = request.session.get('job_type', 'full_time')
            department = request.session.get('department', '')
            min_experience = request.session.get('min_experience', 0)
            max_experience = request.session.get('max_experience', 0)
            min_salary = request.session.get('min_salary', 0.0)
            max_salary = request.session.get('max_salary', 0.0)
            salary_currency = request.session.get('salary_currency', 'EUR')
            skills_required = request.session.get('skills_required', '')
            job_description = form.cleaned_data['job_description']
            job_status = request.session.get('job_status', 'open')  # This was collected in Step 2
            is_remote = request.session.get('is_remote', False)  # If applicable

            # Save the data to the database
            job_post = JobPost(
                title=title,
                company=company,
                country=country,
                state_province=state_province,
                city=city,
                job_type=job_type,
                department=department,
                min_experience=min_experience,
                max_experience=max_experience,
                min_salary=min_salary,
                max_salary=max_salary,
                salary_currency=salary_currency,
                skills_required=skills_required,
                job_description=job_description,
                status=job_status,
                is_remote=is_remote,  # Save the is_remote field
            )
            job_post.save()

            # Optionally, clear session data if not needed anymore
            request.session.flush()

            # Redirect to a summary or success page
            return redirect('job_create_summary')  # This is a hypothetical summary page
    else:
        form = JobPostFormStep3()

    return render(request, 'recruiter/job_form_step3.html', {'form': form})
