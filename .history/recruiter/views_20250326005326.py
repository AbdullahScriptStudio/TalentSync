from django.shortcuts import render, redirect
from .models import JobPost
#from .forms import JobPostForm  # We'll create this form next
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .forms import JobPostForm




# View to list all job posts
def job_list(request):
    job_posts = JobPost.objects.all()
    return render(request, 'recruiter/job_list.html', {'job_posts': job_posts})

# View to show details of a single job post
def job_detail(request, pk):
    job_post = JobPost.objects.get(pk=pk)
    return render(request, 'recruiter/job_detail.html', {'job_post': job_post})


#testing




def job_create_combined(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            # Set job_status to 'open' by default
            job_post = form.save(commit=False)
            job_post.status = 'open'  # Set the status to 'open'
            job_post.save()
            return redirect('job_list')  # Redirect after saving the job post
    else:
        form = JobPostForm()

    return render(request, 'recruiter/job_form_combined.html', {'form': form})



def job_post_success(request):
    return 


def job_list(request):
    # Get all jobs, ordered by creation date (or you can change it to your preference)
    job_posts = JobPost.objects.all().order_by('-posted_at')

    # Paginate the job list (8 items per page)
    paginator = Paginator(job_posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # If there are no jobs, display the 'No active jobs' message and hide pagination
    if not page_obj.has_other_pages():
        show_pagination = False
    else:
        show_pagination = True

    return render(request, 'recruiter/job_list.html', {
        'page_obj': page_obj,
        'show_pagination': show_pagination
    })


def job_description(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    return render(request, 'recruiter/job_description.html', {'job': job})


def job_edit(request, id):
    job = get_object_or_404(JobPost, id=id)

    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_description', id=job.id)  # Redirect to the job description page after saving
    else:
        form = JobPostForm(instance=job)

    return render(request, 'recruiter/job_edit.html', {'form': form, 'job': job})