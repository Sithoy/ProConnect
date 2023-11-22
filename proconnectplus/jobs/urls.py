

from django.urls import path
from .views import job_list, create_job

app_name="jobs"

urlpatterns = [
    path('', job_list, name='job_list'),
    path('create/', create_job, name='create_job'),
    # ... other job-related URLs ...
]
