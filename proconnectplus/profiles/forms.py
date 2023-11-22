from django import forms
from .models import PersonalProfile
# , ProfessionalProfile, InstitutionalProfile

class PersonalProfileForm(forms.ModelForm):
    class Meta:
        model = PersonalProfile
        fields = ['contact', 'resume', 'bio', 'skills', 'education', 'work_experience']
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'skills': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'education': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
            'work_experience': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        }

# class ProfessionalProfileForm(forms.ModelForm):
#     class Meta:
#         model = ProfessionalProfile
#         fields = ['professional_title', 'professional_bio', 'linkedin_profile', 'publications_portfolio']

# class InstitutionalProfileForm(forms.ModelForm):
#     class Meta:
#         model = InstitutionalProfile
#         fields = ['name', 'institution_type', 'contact_info', 'description', 'website', 'industry', 'size']
