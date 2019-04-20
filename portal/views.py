from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login   #as it clashes with other login term
from .forms import *  

def home(request):
    context = {}
    return render(request, 'portal/home.html', context)