from survey import views
from django.urls import path

urlpatterns = [
    # localhost:8099/address/
    path('', views.home),
    #path('survey/',)
    #path('success', views.home),
    path('save_survey', views.save_survey),
    # 결과 페이지로 가는 url이 필요
    path('show_result',views.show_result),
    # jQuery Mobile 을 위한 페이지
    path('show_result2',views.show_result2),


]