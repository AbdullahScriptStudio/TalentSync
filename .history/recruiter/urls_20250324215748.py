from django.urls import path
from .views import JobPostListView, JobPostDetailView, JobPostCreateView, JobPostUpdateView, JobPostDeleteView

urlpatterns = [
    path('', JobPostListView.as_view(), name='job_list'),  # List all jobs
    path('<int:pk>/', JobPostDetailView.as_view(), name='job_detail'),  # View job details
    path('<int:pk>/edit/', JobPostUpdateView.as_view(), name='job_edit'),  # Edit job
    path('<int:pk>/delete/', JobPostDeleteView.as_view(), name='job_delete'),  # Delete job
]
