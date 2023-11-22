from django.shortcuts import redirect, render

from .forms import JobForm
from .models import Job

def job_list(request):
    jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'job_list.html', {'jobs': jobs})


def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:job_list')  # Redirect to the job list view after saving
    else:
        form = JobForm()

    return render(request, 'create_job.html', {'form': form})