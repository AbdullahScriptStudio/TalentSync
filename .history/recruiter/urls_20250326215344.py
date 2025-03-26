from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    #adding new job
    #path('create/step1/', views.job_create_step1, name='job_create_step1'),
    #path('create/step2/', views.job_create_step2, name='job_create_step2'),
    #path('create/step3/', views.job_create_step3, name='job_create_step3'),
    path('job/post/', views.job_create_combined, name='# The `job_create_combined` function is a view
    # that combines the functionality of creating a
    # job in multiple steps into a single step.
    # Instead of having separate views for each
    # step of creating a job (like
    # `job_create_step1`, `job_create_step2`,
    # `job_create_step3`), the
    # `job_create_combined` view handles the entire
    # job creation process in one go. This can
    # streamline the user experience by reducing
    # the number of steps required to create a job
    # posting.
    job_create_combined'),
    #path('create/success/', views.job_post_success, name='job_post_success'), #to show job posted successfully
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/description/<int:job_id>/', views.job_description, name='job_description'),
    path('job/edit/<int:id>/', views.job_edit, name='job_edit'),
    path('job/delete/<int:id>/', views.job_delete, name='job_delete'),
    path('dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)