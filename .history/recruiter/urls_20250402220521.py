from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import handler404, handler500
from . import views

handler404 = 'yourapp.views.custom_404'  # Replace 'yourapp' with your actual app name
handler500 = 'yourapp.views.custom_500'

urlpatterns = [
    
    #adding new job
    #path('create/step1/', views.job_create_step1, name='job_create_step1'),
    #path('create/step2/', views.job_create_step2, name='job_create_step2'),
    #path('create/step3/', views.job_create_step3, name='job_create_step3'),
    path('job/post/', views.job_create_combined, name='job_create_combined'),
    #path('create/success/', views.job_post_success, name='job_post_success'), #to show job posted successfully
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/description/<int:job_id>/', views.job_description, name='job_description'),
    path('job/edit/<int:id>/', views.job_edit, name='job_edit'),
    path('job/delete/<int:id>/', views.job_delete, name='job_delete'),
    path('dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('applications/', views.applications_list, name='applications_list'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)