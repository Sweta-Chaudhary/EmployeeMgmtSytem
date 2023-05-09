
from django.shortcuts import render
from django.contrib.auth.models import User
from employee.models import *



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
    return render(request, 'login.html')


def login_home(request):
    return render(request, 'login_home.html')
