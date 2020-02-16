from address import views # 하나의 컨트롤러 역할을 한다
from django.urls import path


# 요청이 오면 특정 함수를 호출해서 요청을 처리하라는 의미가 되도록 디자인 해야한다
urlpatterns = [
    # localhost:8099/address/
    path('', views.home),
    # 등록 폼으로 가는 url과 모델
    path('write', views.write), # select 할 수 있게 어떻게?
    # 입력 (insert 처리하는 곳)
    path('insert', views.insert),
    # 상세 페이지
    path('detail', views.detail),
    # 수정 처리
    path('update', views.update),
    # 삭제 처리
    path('delete', views.delete),

    path('chart2', views.chart2),

    path('chart3', views.chart3),
]