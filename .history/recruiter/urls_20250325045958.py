from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.JobPostListView.as_view(), name='job_list'),  # List all jobs
    path('<int:pk>/', views.JobPostDetailView.as_view(), name='job_detail'),  # View job details
    path('<int:pk>/edit/', views.JobPostUpdateView.as_view(), name='job_edit'),  # Edit job
    path('<int:pk>/delete/', views.JobPostDeleteView.as_view(), name='job_delete'),  # Delete job
    
    #adding new job
    path('create/step1/', views.job_create_step1, name='job_create_step1'),
    path('create/step2/', views.job_create_step2, name='job_create_step2'),
    path('create/step3/', views.job_create_step3, name='job_create_step3'),
]
