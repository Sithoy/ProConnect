# profiles/urls.py

from django.urls import path
from .views import create_edit_personal_profile

app_name = 'profiles'

urlpatterns = [
    path('personal/create-edit/', create_edit_personal_profile, name='create_edit_personal_profile'),
    # ... other URL patterns ...
]
