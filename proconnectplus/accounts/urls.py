from django.urls import path
from . import views
from .views import user_login, user_logout

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # Add other URLs here
]