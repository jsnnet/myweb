from django.urls import path
from . import views

urlpatterns = [
    # finalProject/ 뒤에 아무것도 안 붙여도 홈 화면으로 출력되도록 변경ㄴ
    path('', views.home),
    # 로그인 첫화면
    path('join', views.join),
    # sqlite & oracle DB 동시 회원가입
    path('join_Oraclite', views.join_Oraclite),
    # 로그인 버튼 누르면 로그인 폼으로 이동
    path('login', views.login),
    # 로그인 폼으로 이동하여 정보 입력 후 버튼 누르면 세션에 등록
    path('login_session', views.login_session),

    path('logout',views.logout),
    path('qna',views.qna),
    path('myquestion',views.myquestion),
    path('notice1',views.notice1),
    path('ride1',views.ride1),
    path('race1',views.race1),
    path('footer',views.footer),
    path('rideintro1', views.rideintro1),
    path('rideintro2', views.rideintro2),
    path('riderecom1', views.riderecom1),
    path('recom_list', views.recom_list),
    path('raceintro1', views.raceintro1),
    path('whoiszoo1', views.whoiszoo1),
    path('whoispick1', views.whoispick1),
    path('todayzoo1', views.todayzoo1),
    path('countdown', views.countdown),

    # 검색 기능
    path('rideSearch', views.rideSearch, name='rideSearch'),

    # 페이징
    path('index', views.index, name='page'),
    path('home', views.home, name='paging'),

    # 리뷰
    path('review', views.review),
]