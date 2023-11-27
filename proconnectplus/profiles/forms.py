# profiles/forms.py

from django import forms
from .models import PersonalProfile

class PersonalProfileForm(forms.ModelForm):
    class Meta:
        model = PersonalProfile
        fields = ['first_name', 'last_name', 'profile_picture', 'contact', 'resume', 'bio', 'skills', 'education', 'work_experience']
