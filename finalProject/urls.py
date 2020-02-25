from django.urls import path
from . import views

urlpatterns = [
    # finalProject/ 뒤에 아무것도 안 붙여도 홈 화면으로 출력되도록 변경
    path('', views.home),
    # 메뉴에서 홈을 눌렀을때 대문 페이지로 가기
    path('home', views.home),
    # 로그인 첫화면
    path('join', views.join),
    # sqlite & oracle DB 동시 회원가입
    path('join_Oraclite', views.join_Oraclite),
    # 로그인 버튼 누르면 로그인 폼으로 이동
    path('login', views.login),
    # 로그인 폼으로 이동하여 정보 입력 후 버튼 누르면 세션에 등록
    path('login_session', views.login_session),

    path('logout',views.logout),

    #문의사항
    path('qna',views.qna),
    path('qna_up', views.qna_up),
    path('myquestion', views.myquestion),
    path('myq_view', views.myq_view),
    path('myq_delete', views.myq_delete),

    #공지사항
    path('notice1',views.notice1),
    path('notice_detail', views.notice_detail),

    # 승마 소개
    path('ride1',views.ride1),

    # 경마 소개
    path('race1',views.race1),

    # 승마장 소개
    path('rideintro1', views.rideintro1),
    path('rideintro2', views.rideintro2), # 테스트 용

    # 승마장 추천
    path('riderecom1', views.riderecom1),
    path('recom_list', views.recom_list),

    # 렛츠런파크 제주 소개 (경마장 소개)
    path('raceintro1', views.raceintro1),

    path('footer',views.footer),
    path('whoiszoo1', views.whoiszoo1),
    path('whoispick1', views.whoispick1),
    path('todayzoo1', views.todayzoo1),
    path('countdown', views.countdown),

    # 검색 기능
    path('rideSearch', views.rideSearch, name='rideSearch'),

    # 리뷰
    path('review', views.review),
    path('up_review', views.up_review),
    path('write_review2', views.write_review2),
]