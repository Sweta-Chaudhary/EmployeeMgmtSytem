
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == 'POST':
        name = request.POST('name')
        empcode = request.POST('empcode')
        email = request.POST('email')
        pwd = request.POST('pwd')
        

        try:
            user =  User.objects.create_user(name=name, empcode=empcode, email=email, pwd=pwd)
            EmployeeDetail.objects.create(user = user , empcode=empcode)
            error="no"
        except:
            error="yes"    

        return render(request, 'registration.html',locals())

def login(request):
    error=""

    if request.method == 'POST':
        name = request.POST('name')
        pwd = request.POST('pwd')


        user = authenticate(username=name, password=pwd)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    return render(request, 'login.html')


def login_home(request):
    return render(request, 'login_home.html')
