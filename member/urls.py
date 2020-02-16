from django.urls import path
from member import views
from django.contrib import admin
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    #회원 가입에 대한 액션 추가
    path("join", views.join),
    #logout
    path('logout', views.logout, name='logout'),
    #loginform
    path('login', views.loginform, name='login'),
]