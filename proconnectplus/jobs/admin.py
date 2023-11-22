from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'date_posted')
    list_filter = ('date_posted', 'company')
    search_fields = ('title', 'description', 'company', 'location')

admin.site.register(Job, JobAdmin)