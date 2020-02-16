# from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
# from .forms import UserForm,LoginForm
# # Create your views here.
#
# def home(request):
#     return render(request, "member/index.html")
#
# def join(request):
#     # 자동으로 회원 가입 폼 생성된다
#     form = UserForm
#     # 아래의 form 은 폼을 내장하고 있는 객체이다.
#     return render(request, "member/join.html", {"form":form})
# 위에는 하는 과정 중에 하던 것

from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.shortcuts import redirect
# Create your views here.
#시작페이지
def home(request):
    # loginform status => annomynous 가 직힌다 로그인 하지 않았다면
    # is_authenticated : 로그인 여부에 따라서 True/False 로 구분된다
    if not request.user.is_authenticated:
        data = {"username":request.user,
                "is_authenticated":request.user.is_authenticated}

    else: # 로그인 한 상태
        data = {"last_login":request.user.last_login,
                "username":request.user.username,
                "password":request.user.password,
                "is_authenticated":request.user.is_authenticated}

    # context 는 Template 페이지에 전달할 때 사용하는 변수 값

    return render(request,"member/index.html", context={"data":data})

# 회원가입폼과 로그인 폼을 불러옴 .은 현재 디렉토리에있는 forms 모듈에서
# 두 클래스를 불러 와라.

from .forms import UserForm,LoginForm
from django.contrib import auth
@csrf_exempt
def join(request):
    if request.method == "POST": # POST이면 이걸 실행하고 아니면 아래 else 부분 실행하라는 의미
        form = UserForm(request.POST)
        #입력값에 문제가 없으면(모든 유효성 검증 규칙을 통과할 때)
        # 회원 가입 -> 가입처리 후 로그인 세션을 등록 auth.login -> index.html (로그인 했냐 안했냐를 판단) -> 그리고 최종적으로 home다 으로 보낸
        if form.is_valid(): #vaidation 체크를 직접한다
            # form.cleaned_data
            # 검증에 성공한 값들을 딕셔너리 타입으로 저장하고 있는 데이터
            # ** keyword argument, 키워드 인자 (이름으로 호출할 수있는 매개변수)
            # 새로운 사용자가 생성됨
            new_user = User.objects.create_user(**form.cleaned_data)
            #로그인 처리
            auth.login(request,new_user)
            #시작 페이지로 이동
            return redirect("home")
        else:
            render(request,"member/index.html",{"msg":"회원가입 실패!"})
    else: # GET 방식으로 보냈을 때에는 여기로
        form = UserForm() #회원가입 폼 객체를 생성
        # join.html로 넘어가서 출력됨, 폼을 내장하고 있는 객체를 전달한다.
        return render(request, "member/join.html", {"form": form})
    return render(request,"member/index.html")

def logout(request):
    auth.logout(request)
    return redirect("home")

def loginform(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST["username"]
        pwd = request.POST["password"]
        #인증함수, 로그인을 체크해주는 함수이다. 암호화가 되어서 체크해준다.
        user = auth.authenticate(username=name, password=pwd)
        if user is not None: # 인증완료 되었다면
            auth.login(request, user) #로그인 세션 등록
            return redirect("home")
        else: #인증 실패
            return render(request, "member/index.html", {"msg": "로그인 실패!"})
    else:
        form = LoginForm()
        return render(request, "member/loginform.html",{"form":form})

