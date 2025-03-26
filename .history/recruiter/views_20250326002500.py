from django.shortcuts import render, redirect
from .models import JobPost
#from .forms import JobPostForm  # We'll create this form next
from .forms import JobPostFormStep1, JobPostFormStep2, JobPostFormStep3
from django.core.paginator import Paginator



# View to list all job posts
def job_list(request):
    job_posts = JobPost.objects.all()
    return render(request, 'recruiter/job_list.html', {'job_posts': job_posts})

# View to show details of a single job post
def job_detail(request, pk):
    job_post = JobPost.objects.get(pk=pk)
    return render(request, 'recruiter/job_detail.html', {'job_post': job_post})


#testing
from .forms import JobPostForm




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
    # Fetch all job posts, ordered by creation date
    jobs = JobPost.objects.all().order_by('-posted_at')

    # Set up pagination: 8 jobs per page
    paginator = Paginator(jobs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recruiter/job_list.html', {'page_obj': page_obj})


def job_description(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)  # Fetch the job using the job_id
    return render(request, 'recruiter/job_description.html', {'job': job})