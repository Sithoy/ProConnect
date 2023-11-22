from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# SignUp Process

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in and redirect to a new page
            login(request, user)
            return redirect('some_view')  # Redirect to a desired page after registration
    else:
        form = UserCreationForm()  

def register(request):
    # Logic for registration
    form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

# Login Process

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            # Return an 'invalid login' error message
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')

