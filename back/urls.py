from django.contrib import admin
from django.urls import path
from back import views

urlpatterns = [
    path('basic',views.basic),
    path('home', views.home),
    path('example',views.example),
    path('reserve',views.reserve),
    path('reserve2',views.reserve2),
    path('reserve3',views.reserve3),
    path('reserve4',views.reserve4),
    path('starter',views.starter),
    path('dashboard',views.dashboard),
    path('signin',views.signin),
    path('foodfun_index',views.foodfun_index),

]