from django.urls import path
from . import views

urlpatterns = [
    path('home1', views.home1, name="home"),
    path('join', views.join),
    path('join2', views.join2),
    path('join3', views.join3),
    path('login', views.login),
    path('login2',views.login2),
    path('login4',views.login4),
    # path('login3',views.login3),
    # path('login5',views.login5),
    path('login5',views.login5, name="login_success"),

    path('logout',views.logout),
    path('logout5',views.logout5),
    path('qna1',views.qna1),
    path('myquestion',views.myquestion),
    path('notice1',views.notice1),
    path('ride1',views.ride1),
    path('race1',views.race1),
    path('header3',views.header3),
    path('footer',views.footer),
    path('rideintro1', views.rideintro1),
    path('riderecom1', views.riderecom1),
    path('recom_list', views.recom_list),
    path('raceintro1', views.raceintro1),
    path('whoiszoo1', views.whoiszoo1),
    path('whoispick1', views.whoispick1),
    path('todayzoo1', views.todayzoo1),
    path('countdown', views.countdown),
]