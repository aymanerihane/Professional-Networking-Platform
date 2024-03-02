# Create your views here.
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse


import datetime

def index(request):
    context = {
    }
    return render(request,'PNP/index.htm' , context)

