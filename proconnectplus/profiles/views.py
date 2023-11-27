from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PersonalProfileForm
from .models import PersonalProfile
from django.contrib.auth.models import User

@login_required
def create_edit_personal_profile(request):
    try:
        personal_profile = request.user.personal_profile
    except PersonalProfile.DoesNotExist:
        personal_profile = None

    if request.method == 'POST':
        form = PersonalProfileForm(request.POST, request.FILES, instance=personal_profile)
        if form.is_valid():
            personal_profile = form.save(commit=False)
            personal_profile.user = request.user
            personal_profile.save()
            return redirect('profiles:view_personal_profile')  # Redirect to the profile view
    else:
        form = PersonalProfileForm(instance=personal_profile)

    return render(request, 'personal_profile_form.html', {'form': form})

@login_required
def view_personal_profile(request):
    personal_profile = get_object_or_404(PersonalProfile, user=request.user)
    return render(request, 'personal_profile_detail.html', {'personal_profile': personal_profile})
