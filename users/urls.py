from django.urls import path
from . import views

urlpatterns = [
    path('home1', views.home1),
    path('join', views.join),
    path('login', views.login),
    path('logout', views.logout),
    path('qna1',views.qna1),
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
    #설문조사
    path('survey_form', views.survey_form),
    path('save_survey', views.save_survey),
    # 결과 페이지로 가는 url이 필요
    path('show_result',views.show_result),
    # jQuery Mobile 을 위한 페이지
    path('show_result2',views.show_result2),

]