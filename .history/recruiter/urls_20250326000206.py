from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    
    #adding new job
    #path('create/step1/', views.job_create_step1, name='job_create_step1'),
    #path('create/step2/', views.job_create_step2, name='job_create_step2'),
    #path('create/step3/', views.job_create_step3, name='job_create_step3'),
    path('job/post/', views.job_create_combined, name='job_create_combined'),
    path('create/success/', views.job_post_success, name='job_post_success')
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)