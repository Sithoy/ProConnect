# profiles/urls.py

from django.urls import path
from .views import create_edit_personal_profile, view_personal_profile

app_name = 'profiles'

urlpatterns = [
    path('personal/edit/', create_edit_personal_profile, name='create_edit_personal_profile'),
    path('personal/view/', view_personal_profile, name='view_personal_profile'),
]