"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from config import views
from django.views.generic import RedirectView

urlpatterns = [
    # py manage.py runserver 8099 (원하는 port 지정)
    path('admin/', admin.site.urls), # admin 사이트의 url 로 가라는 의미
    #http://localhost:8099/
    #path('',views.home), # 위에 import views 해주면 활성화된다.
    #finalProject
    path('finalProject/',include('finalProject.urls')),
    #start url 수정
    path('', RedirectView.as_view(url='/finalProject/', permanent=True)),
]
