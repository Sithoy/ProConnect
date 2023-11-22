from django.urls import path
from .views import event_list, create_event

app_name="events"

urlpatterns = [
    path('', event_list, name='event_list'),
    path('create/', create_event, name='create_event'),
    # ... other event-related URLs ...
]
