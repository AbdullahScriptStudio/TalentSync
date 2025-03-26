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
            # Collect data from the form and save to session
            job_type = form.cleaned_data['job_type']
            department = form.cleaned_data['department']
            min_experience = form.cleaned_data['min_experience']
            max_experience = form.cleaned_data['max_experience']
            min_salary = form.cleaned_data['min_salary']
            max_salary = form.cleaned_data['max_salary']
            salary_currency = form.cleaned_data['salary_currency']
            skills_required = form.cleaned_data['skills_required']
            job_status = form.cleaned_data['job_status']
            
            # Save the collected data to session
            request.session['job_type'] = job_type
            request.session['department'] = department
            request.session['min_experience'] = min_experience
            request.session['max_experience'] = max_experience
            request.session['min_salary'] = min_salary
            request.session['max_salary'] = max_salary
            request.session['salary_currency'] = salary_currency
            request.session['skills_required'] = skills_required
            request.session['job_status'] = job_status

            # Debugging: print to check if data is saved in the session
            print(f"Session Data for Step 2: {request.session.items()}")

            # Redirect to step 3 after saving data in session
            return redirect('job_create_step3')  # Make sure this URL points to step 3
    else:
        form = JobPostFormStep2()

    return render(request, 'recruiter/job_form_step2.html', {'form': form})


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
            job_type = request.session.get('job_type', 'full_time')  # Step 2 Data
            department = request.session.get('department', '')
            min_experience = request.session.get('min_experience', 0)
            max_experience = request.session.get('max_experience', 0)
            min_salary = request.session.get('min_salary', 0.0)
            max_salary = request.session.get('max_salary', 0.0)
            salary_currency = request.session.get('salary_currency', 'EUR')
            skills_required = request.session.get('skills_required', '')
            job_description = form.cleaned_data['job_description']
            job_status = request.session.get('job_status', 'open')  # Step 2 Data

            # Debugging: Check if session data is being collected
            print(f"Session Data for Step 3: {request.session.items()}")

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
                status=job_status
            )
            job_post.save()

            # Optionally, clear session data after saving
            request.session.flush()

            # Redirect to a success or summary page
            return redirect('job_create_summary')  # Adjust this to your success/summary page URL
    else:
        form = JobPostFormStep3()

    return render(request, 'recruiter/job_form_step3.html', {'form': form})


#testing
from .forms import JobPostForm


def job_create_combined(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_post_data = form.cleaned_data

            job_post = JobPost(
                title=job_post_data['title'],
                company=job_post_data['company'],
                country=job_post_data['country'],
                state_province=job_post_data['state_province'],
                city=job_post_data['city'],
                job_type=job_post_data['job_type'],
                department=job_post_data['department'],
                min_experience=job_post_data['min_experience'],
                max_experience=job_post_data['max_experience'],
                min_salary=job_post_data['min_salary'],
                max_salary=job_post_data['max_salary'],
                salary_currency=job_post_data['salary_currency'],
                skills_required=job_post_data['skills_required'],
                job_description=job_post_data['job_description'],
                job_status=job_post_data['job_status'],
            )
            job_post.save()

            # After successful save, redirect to a success page
            return redirect('job_post_success')  # Change to your success page URL
        else:
            print(form.errors)  # This will help debug any form validation issues
    else:
        form = JobPostForm()

    return render(request, 'recruiter/job_post_create.html', {'form': form})



def job_post_success(request):
    return 