from django.urls import path
from . import views
from .views import create_post

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/create/', create_post, name='create_post'),
    # Add other blog-related URLs here
]
