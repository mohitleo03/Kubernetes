from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index (request):
#     return HttpResponse("<h1>Hello from Django...</h1>")

# def index (request):
#     name = 'Mohit'
#     return render(request, 'index.html',context={'name' : name})

def index (request):
    name = 'Mohit'
    return render(request, 'login.html')

def login(request):
    username = request.GET['u_name']
    password = request.GET['u_password']
    if username == 'mohit' and password == 'mohit03':
        msg = 'Login successful'
    else:
        msg = "Login Failed"
    return render(request,'index.html',context={'msg':msg, 'name':username})