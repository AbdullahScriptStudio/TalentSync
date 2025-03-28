from django.urls import path
from .views import applicant_dashboard

urlpatterns = [
    path('dashboard/', applicant_dashboard, name='applicant_dashboard'),
]
