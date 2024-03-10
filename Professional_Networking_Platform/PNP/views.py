# Create your views here.
from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User,UserForm,LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login

# import datetime
# @login_required



def index(request):
    context = {
    }
    return render(request,'PNP/index.htm' , context)

def signUp(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Ne pas sauvegarder immédiatement pour modifier le mot de passe
            user.password = make_password(form.cleaned_data['password'])  # Utilisez make_password pour sécuriser le mot de passe
            user.save()
            return HttpResponse("User Created")
    else:
        form = UserForm()
    return render(request, 'registration/signUp.html', {"form": form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashed_password = make_password(password)
            print(hashed_password)
            user = authenticate(request, email=email, password=hashed_password)
            if user is not None:
                auth_login(request, user)
                print("User is authenticated")
                redirect('PNP:index')
            else:
                # Handle invalid login credentials here
                # For example, you could display an error message
                # and render the login page again
                print("User is not authenticated")
                error_message = "Invalid email or password. Please try again."
                return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})