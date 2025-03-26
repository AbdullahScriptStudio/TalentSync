from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('job/post/', views.job_create_combined, name='job_create_combined'),
    path('create/success/', views.job_post_success, name='job_post_success'), #to show job posted successfully
    path('list/', views.job_list, name='job_list')
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)