# events/views.py

from django.shortcuts import redirect, render
from .models import Event
from .forms import EventForm

def event_list(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'event_list.html', {'events': events})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:event_list')  # Redirect to the event list view after saving
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})