from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from datetime import timedelta
from recruiter.models import Application, JobPost  # Ensure JobPost is imported

@login_required
def applicant_dashboard(request):
    user = request.user

    # Ensure only applicants access this page
    if user.role != "applicant":
        return render(request, "error.html", {"message": "Access Denied"})

    applications = Application.objects.filter(applicant_email=user.email).order_by("-applied_at")
    total_applications = applications.count()

    # Job Application Trend (Last 6 Months)
    last_six_months = [now().replace(day=1) - timedelta(days=30 * i) for i in reversed(range(6))]
    months = [date.strftime("%b") for date in last_six_months]

    application_counts = [
        applications.filter(applied_at__year=date.year, applied_at__month=date.month).count()
        for date in last_six_months
    ]

    # Fetch a few job postings to display on the dashboard
    recent_jobs = JobPost.objects.filter(status='open').order_by('-posted_at')[:5]  # Get the latest 5 open jobs

    context = {
        "applicant_name": user.first_name or user.username,
        "profile_picture": user.profile_pic.url if user.profile_pic else "/static/images/profile.png",
        "total_applications": total_applications,
        "applications": applications,
        "application_dates": months,
        "application_counts": application_counts,
        "recent_jobs": recent_jobs,  # Add recent jobs to the context
    }

    return render(request, "applicant/applicant_dashboard.html", context)




#job list
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from recruiter.models import JobPost

@login_required
def applicant_job_list(request):
    # Fetch all job posts
    job_posts = JobPost.objects.filter(status='open').order_by('-posted_at')

    print(f"Jobs found: {job_posts.count()}")  # Debugging: Check if jobs exist

    paginator = Paginator(job_posts, 8)  # Show 8 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'applicant_name': request.user.first_name or request.user.username,
        'profile_picture': request.user.profile_pic.url if request.user.profile_pic else "/static/images/profile.png",
    }
    
    return render(request, 'applicant/applicant_job_list.html', context)




#job description
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from recruiter.models import JobPost

@login_required
def applicant_job_description(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    context = {
        'job': job,
        'applicant_name': request.user.first_name or request.user.username,
        'profile_picture': request.user.profile_pic.url if request.user.profile_pic else "/static/images/profile.png",
    }
    return render(request, 'applicant/applicant_job_description.html', context)



#application for jobs
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from recruiter.models import Application, JobPost
from .forms import ApplicationForm  # Import the form

@login_required
def apply_on_job(request, job_id):
    job_post = get_object_or_404(JobPost, id=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_post = job_post
            application.applicant_name = request.user.username  # Get the applicant's name
            application.applicant_email = request.user.email  # Get the applicant's email
            application.save()
            return redirect('applicant_job_list')  # Redirect to job list or a success page
    else:
        form = ApplicationForm()

    return render(request, 'applicant/apply_on_job.html', {'form': form, 'job_post': job_post})