# render 가져올 것
from django.shortcuts import render,redirect
# 위에는 forward 와 redirect 개념

# django 사이트에서 최상위 페이지(documentRoot) 에 대한 요청을 처리

def home(request):
    msg = "안녕하세요, 여기는 메인 페이지 입니다. :)"
    name = "홍길동"
    age = 20
    # render : MVC 패턴에서 사용했던 forward 개념이다
    # Template의 html 에게 값을 전달하는 방식이 딕셔너리
    # 이게 전체 페이지의 index 페이지가 될 것이다
    return render(request,"index.html", {'msg':msg, 'name':name, 'age':age})