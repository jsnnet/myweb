from shop import views # 하나의 컨트롤러 역할을 한다
from django.urls import path


# 요청이 오면 특정 함수를 호출해서 요청을 처리하라는 의미가 되도록 디자인 해야한다
urlpatterns = [

    path("product_list",views.product_list, name='product_list'),
    # 오늘은 admin 등록 없이 사용할 것이다.
    path("product_write",views.product_write),
    path("product_insert",views.product_insert),
    path("product_detail",views.product_detail),
]