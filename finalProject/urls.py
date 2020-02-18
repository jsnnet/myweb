from django.urls import path
from . import views

urlpatterns = [
    path('home1', views.home1),
    path('join', views.join),
    path('join2', views.join2),
    path('login', views.login),
    path('login2',views.login2),
    # path('login3',views.login3),
    path('logout',views.logout),
    path('qna1',views.qna1),
    path('myquestion',views.myquestion),
    path('notice1',views.notice1),
    path('ride1',views.ride1),
    path('race1',views.race1),
    path('header3',views.header3),
    path('footer',views.footer),
    path('rideintro1', views.rideintro1),
    path('riderecom1', views.riderecom1),
    path('raceintro1', views.raceintro1),
    path('whoiszoo1', views.whoiszoo1),
    path('whoispick1', views.whoispick1),
    path('todayzoo1', views.todayzoo1),
    path('countdown', views.countdown),
]