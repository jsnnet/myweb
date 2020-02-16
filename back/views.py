from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request,"back/index.html")

def basic(request):
    return render(request,"back/basic.html")

def example(request):
    return render(request,"back/example.html")

def reserve(request):
    return render(request,"back/reserve.html")

def reserve2(request):
    return render(request,"back/reserve2.html")

def reserve3(request):
    return render(request,"back/reserve3.html")

def reserve4(request):
    return render(request,"back/reserve4.html")

def starter(request):
    return render(request,"back/starter.html")

def dashboard(request):
    return render(request,"back/dashboard.html")

def signin(request):
    return render(request,"back/signin.html")

def foodfun_index(request):
    return render(request,"back/foodfun_index.html")