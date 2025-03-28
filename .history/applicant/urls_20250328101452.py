from django.urls import path
from .views import applicant_dashboard
from . import views

urlpatterns = [
    path('dashboard/', applicant_dashboard, name='applicant_dashboard'),
    path('job-list/', views.applicant_job_list, name='applicant_job_list'),
    path('job-description/<int:job_id>/', views.applicant_job_description, name='applicant_job_description'),
    path('applicant/apply/<int:job_id>/', views.apply_on_job, name='apply_on_job'),
    path('applied-jobs/', views.applied_job_list, name='applied_job_list'),
    path('applied-jobs/<int:application_id>/', applied_job_description, name='applied_job_description'),



]
