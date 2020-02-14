from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def home1(request):
    return render(request, "users/home1.html")


def join(request):
    # if request.method == "POST":
    #     if request.POST["password1"] == request.POST["password2"]:
    #         user = User.objects.create_user(
    #             username=request.POST["username"],password=request.POST["password1"])
    #         auth.login(request,user)
    #         return redirect('home')
    #     return render(request, 'users/join.html')
    return render(request, "users/join.html")


def login(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(request, username=username, password=password)
    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect('home')
    #     else:
    #         return render(request, 'login.html', {'error': 'username or password is incorrect'})
    # else:
    return render(request, "users/login.html")


def logout(request):
    # auth.logout(request)
    return render(request, "users/home1.html")

def qna1(request):
    return render(request, "users/qna1.html")

def notice1(request):
    return render(request, "users/notice1.html")

def ride1(request):
    return render(request, "users/ride1.html")

def race1(request):
    return render(request, "users/race1.html")

def header3(request):
    return render(request, "users/header3.html")

def footer(request):
    return render(request, "users/footer.html")

def rideintro1(request):
    return render(request, "users/rideintro1.html")

def riderecom1(request):
    return render(request, "users/riderecom1.html")

def raceintro1(request):
    return render(request, "users/raceintro1.html")

def whoiszoo1(request):
    return render(request, "users/whoiszoo1.html")

def whoispick1(request):
    return render(request, "users/whoispick1.html")

def todayzoo1(request):
    return render(request, "users/todayzoo1.html")

