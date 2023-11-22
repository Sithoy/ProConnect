from django.shortcuts import render

def register(request):
    # Logic for registration
    return render(request, 'register.html')