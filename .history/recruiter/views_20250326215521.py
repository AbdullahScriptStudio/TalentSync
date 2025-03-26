from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from recruiter.forms import JobPostForm
from recruiter.models import JobPost
from people.models import CustomUser  # Import the user model

def is_recruiter(user):
    """Helper function to check if the user is a recruiter."""
    return user.is_authenticated and user.user_type == "recruiter"

# 🔹 Recruiter Dashboard (Shows Only Recruiter's Jobs)
@login_required
def recruiter_dashboard(request):
    if not is_recruiter(request.user):
        messages.error(request, "Unauthorized access.")
        return redirect('job_list')  # Redirect applicants to job listings

    recruiter = request.user
    total_jobs = JobPost.objects.filter(recruiter=recruiter).count()
    total_applicants = 232  # Placeholder (update if needed)

    # Only fetch the recruiter's jobs
    recent_jobs = JobPost.objects.filter(recruiter=recruiter).order_by('-posted_at')[:4]

    # Get job status counts
    open_jobs = JobPost.objects.filter(recruiter=recruiter, status="open").count()
    closed_jobs = JobPost.objects.filter(recruiter=recruiter, status="closed").count()
    paused_jobs = JobPost.objects.filter(recruiter=recruiter, status="paused").count()

    context = {
        "total_jobs": total_jobs,
        "total_applicants": total_applicants,
        "recent_jobs": recent_jobs,
        "open_jobs": open_jobs,
        "closed_jobs": closed_jobs,
        "paused_jobs": paused_jobs,
    }
    return render(request, "recruiter/recruiter_dashboard.html", context)


# 🔹 Job List (Applicants See All, Recruiters See Their Jobs)
@login_required
def job_list(request):
    if is_recruiter(request.user):
        # Show only the recruiter's jobs
        job_posts = JobPost.objects.filter(recruiter=request.user).order_by('-posted_at')
    else:
        # Applicants see all jobs
        job_posts = JobPost.objects.all().order_by('-posted_at')

    paginator = Paginator(job_posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    show_pagination = page_obj.has_other_pages()

    return render(request, 'recruiter/job_list.html', {
        'page_obj': page_obj,
        'show_pagination': show_pagination
    })


# 🔹 Job Creation (Only Recruiters)
@login_required
def job_create_combined(request):
    if not is_recruiter(request.user):
        messages.error(request, "Applicants cannot create jobs.")
        return redirect('job_list')

    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.recruiter = request.user  # Assign recruiter
            job_post.status = 'open'
            job_post.save()
            return redirect('job_list')
    else:
        form = JobPostForm()

    return render(request, 'recruiter/job_form_combined.html', {'form': form})


# 🔹 Job Edit (Only Recruiter Who Created It)

@login_required
def job_edit(request, id):
    job = get_object_or_404(JobPost, id=id)

    # 🚨 Ensure the logged-in recruiter is the job's owner
    if job.recruiter != request.user:
        messages.error(request, "You are not authorized to edit this job.")
        return redirect('recruiter_dashboard')  # Redirect unauthorized users

    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated successfully!")
            return redirect('job_description', job_id=job.id)
        else:
            print(form.errors)  # Debugging errors
    else:
        form = JobPostForm(instance=job)

    return render(request, 'recruiter/job_edit.html', {'form': form, 'job': job})


# 🔹 Job Delete (Only Recruiter Who Created It)
@login_required
def job_delete(request, id):
    job = get_object_or_404(JobPost, id=id)

    # 🚨 Ensure the logged-in recruiter is the job's owner
    if job.recruiter != request.user:
        messages.error(request, "You are not authorized to delete this job.")
        return redirect('recruiter_dashboard')  # Redirect unauthorized users

    job.delete()
    messages.success(request, "Job deleted successfully.")
    return redirect('job_list')


# View to show details of a single job post
def job_detail(request, pk):
    job_post = JobPost.objects.get(pk=pk)
    return render(request, 'recruiter/job_detail.html', {'job_post': job_post})