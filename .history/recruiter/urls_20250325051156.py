from django.urls import path
from . import views
 
urlpatterns = [
    
    
    #adding new job
    path('create/step1/', views.job_create_step1, name='job_create_step1'),
    path('create/step2/', views.job_create_step2, name='job_create_step2'),
    path('create/step3/', views.job_create_step3, name='job_create_step3'),
]
