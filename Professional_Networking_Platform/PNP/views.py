# Create your views here.
from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import SignUpForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login


# import datetime
# @login_required



def index(request):
    context = {
    }
    return render(request,'PNP/index.htm' , context)

def profile(request):
    context = {
    }
    return render(request,'profilePage/profile.html' , context)
def messaging(request):
    context = {
    }
    return render(request,'messagePage/messagePage.html' , context)

def firstPage(request):
    context = {
    }
    return render(request,'firstPage/fisrtPage.html' , context)

def signUp(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponse("User Created")
    else:
        user = UserCreationForm()
    return render(request, 'registration/signUp.html', {"form": user})

def login(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         hashed_password = make_password(password)
    #         print(hashed_password)
    #         user = authenticate(request, username=username, password=hashed_password)
    #         if user is not None:
    #             auth_login(request, user)
    #             print("User is authenticated")
    #             redirect('PNP:index')
    #         else:
    #             # Handle invalid login credentials here
    #             # For example, you could display an error message
    #             # and render the login page again
    #             print("User is not authenticated")
    #             error_message = "Invalid email or password. Please try again."
    #             return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})
    # else:
    #     form = LoginForm()
    return render(request, 'registration/login.html')