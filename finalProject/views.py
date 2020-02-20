from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import cx_Oracle as oci
from django.views.decorators.csrf import csrf_exempt
from .models import JoinForm

# 승마장추천 필터링을 위해 ------------
from django.shortcuts import render
from django.db.models import Q
# from .models import Document
from django.db import models
# -----------------------------------

def home1(request):
    return render(request, "finalProject/home1.html")

def join(request):
    return render(request, "finalProject/join3.html")

# (상) sqlite 과 oracle DB에 동시 회원가입하는 부분====================================
from .forms import LoginForm,UserForm
from django.contrib import auth
@csrf_exempt
def join_Oraclite(request):
    if request.method == "POST":  # POST이면 이걸 실행하고 아니면 아래 else 부분 실행하라는 의미
        form = UserForm(request.POST)
        print("폼 : ", form)
        # 입력값에 문제가 없으면(모든 유효성 검증 규칙을 통과할 때)
        # 회원 가입 -> 가입처리 후 로그인 세션을 등록 auth.login -> index.html (로그인 했냐 안했냐를 판단) -> 그리고 최종적으로 home다 으로 보낸
        if form.is_valid():  # vaidation 체크를 직접한다
            # form.cleaned_data
            # 검증에 성공한 값들을 딕셔너리 타입으로 저장하고 있는 데이터
            # ** keyword argument, 키워드 인자 (이름으로 호출할 수있는 매개변수)
            # 새로운 사용자가 생성됨
            new_user = User.objects.create_user(**form.cleaned_data)
            # 로그인 처리
            auth.login(request, new_user)
            # 시작 페이지로 이동
            return redirect("home1")
        else:
            render(request, "finalProject/home1.html", {"msg": "회원가입 실패!"})
    else:  # GET 방식으로 보냈을 때에는 여기로
        form = UserForm()  # 회원가입 폼 객체를 생성
        # join.html로 넘어가서 출력됨, 폼을 내장하고 있는 객체를 전달한다.
        return render(request, "finalProject/join3.html", {"form": form})
    return render(request, "finalProject/home1.html")

    # 폼 안쓰고 새로 생성한 모델 활용 ==================================================================================
    # sign_up = JoinForm(mid=request.POST['mid'],
    #                mpwd=request.POST['mpwd'],
    #                mname=request.POST['mname'],
    #                mtel=request.POST['mtel'],
    #                madmin=request.POST['madmin']
    #                   )
    # sign_up.save()
    # ================================================================================================================

    # sqlite 에 회원가입 완료
    # oracle 에 회원 가입 시작
    conn = oci.connect('doosun/doosun@192.168.0.126:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute("select*from test_member")
    mid = request.POST.get("mid")
    print("mid : ", mid)
    mpwd = request.POST.get("mpwd")
    print("mpwd : ", mpwd)
    mname = request.POST.get("mname")
    print("mname : ", mname)
    mtel = request.POST.get("mtel")
    print("mtel : ", mtel)
    madmin = request.POST.get("madmin")
    print("madmin : ", madmin)
    if madmin is not None:
        join_insert = "insert into test_member VALUES(test_member_seq.nextVal, :mid, :mpwd, :mname, :mtel, :madmin, sysdate)"
        cursor.execute(join_insert, mid=mid, mpwd=mpwd, mname=mname, mtel=mtel, madmin=madmin)
        cursor.close()
        conn.commit()
        conn.close()
        return render(request, "finalProject/home1.html")
    else:
        return render(request, "finalProject/join3.html")
    return redirect('home')
# (하) sqlite 과 oracle DB에 동시 회원가입하는 부분==============================================================================

def login(request):
    return render(request, 'finalProject/login.html')

def login2(request):
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

# 로그인 하면 session 에 등록
def login_session(request):
    print("html 에서 어떤 갑이 넘어오나 : ", request.POST["mid"])
    mid = request.POST["mid"]
    print("넘어온 아이디 : ", mid)
    request.session['id'] = mid
    print("아이디 세션으로 : ", request.session['id'])
    #request.session['password'] = ' '
    # return HttpResponse("finalProject/home1.html")
    return render(request, "finalProject/home1.html")

# session 확인
# def access_session(request):
#     response = "<h1>Welcome to Sessions of dataflair</h1><br>"
#     if request.session.get('id'):
#         response += "Name : {0} <br>".format(request.session.get('id'))
#         return HttpResponse(response)
#     else:
#         return redirect('login_session')

def logout(request):
    response = render(request, 'finalProject/home1.html')
    response.delete_cookie('mid')
    response.delete_cookie('mpwd')
    auth.logout(request)
    return response

def qna1(request):
    conn = oci.connect('doosun/doosun@192.168.0.126:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from test_member')
    print(cursor.fetchone())
    mid = request.POST.get("mid")
    print("mid : ", mid)
    qtitle = request.POST.get("qtitle")
    print("qtitle : ", qtitle)
    qcontent = request.POST.get("qcontent")
    print("qcontent : ", qcontent)
    if (mid != None):
        sql_insert = 'insert into test_question VALUES(test_question_seq.nextVal, :mid, :qtitle, :qcontent, :qhit, sysdate)'
        cursor.execute(sql_insert, mid=mid, qtitle=qtitle, qcontent=qcontent, qhit = 0)
        conn.commit()
        cursor.execute('select*from test_question')
        print(cursor.fetchall())
        cursor.close()
        conn.close
        return render(request, "finalProject/qna1.html")
    else:
        return render(request, "finalProject/qna1.html")

def myquestion(request):
    conn = oci.connect('doosun/doosun@192.168.0.126:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from test_question')
    qlist = cursor.fetchall()
    # qnum, mid, qtitle, qcontent, qhit, qdate = qlist
    for (qnum, mid, qtitle, qcontent, qhit, qdate) in qlist:
        # print("qlist : ",qlist)
        print("글번호: ", qnum)
        print("회원ID : ",mid)
        print("제목 : ",qtitle)
        print("조회수 : ",qhit)
        print("작성날짜 : ",qdate)
    return render(request, "finalProject/myQlist.html",{"qlist":qlist})

def notice1(request):
    conn = oci.connect('doosun/doosun@192.168.0.126:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from test_notice')
    nlist = cursor.fetchall()
    # qnum, mid, qtitle, qcontent, qhit, qdate = qlist
    # NNUM
    # NTITLE
    # NCONTENT
    # NHIT
    # NDATE
    for (nnum, ntitle, ncontent, nhit, ndate) in nlist:
        # print("qlist : ",qlist)
        print("글번호: ", nnum)
        print("제목 : ", ntitle)
        print("내용 : ", ncontent)
        print("조회수 : ", nhit)
        print("작성날짜 : ", ndate)
    return render(request, "finalProject/notice1.html", {"nlist": nlist})

def ride1(request):
    return render(request, "finalProject/ride1.html")

def race1(request):
    return render(request, "finalProject/race1.html")

def header3(request):
    return render(request, "finalProject/header3.html")

def footer(request):
    return render(request, "finalProject/footer.html")

def rideintro1(request):
    return render(request, "finalProject/rideintro1.html")

def riderecom1(request):
    conn = oci.connect('doosun/doosun@192.168.0.126:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from test_place')
    plist = cursor.fetchall()
    # qnum, mid, qtitle, qcontent, qhit, qdate = qlist
    for (pnum, pname, paddr, ptel, plink, pplace, pdate) in plist:
        # print("qlist : ",qlist)
        print("승마장 번호: ", pnum)
        print("승마장 이름 : ", pname)
        print("주소 : ", paddr)
        print("연락처 : ", ptel)
        print("링크 : ", plink)
        print("부대시설 : ", pplace)
        print("등록날짜 : ", pdate)
    return render(request, "finalProject/riderecom1.html", {"plist": plist})

def raceintro1(request):
    return render(request, "finalProject/raceintro1.html")

def whoiszoo1(request):
    return render(request, "finalProject/whoiszoo1.html")

def whoispick1(request):
    return render(request, "finalProject/whoispick1.html")

def todayzoo1(request):
    return render(request, "finalProject/todayzoo1.html")

def countdown(request):
    return render(request, "finalProject/countdown.html")

def recom_list(request):
    conn = oci.connect('doosun/doosun@192.168.0.126:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from test_place')
    rsearch = cursor.fetchall()
    print("포스트 대신에 출력 해볼 : ",rsearch)
    # r = request.GET.get()
    q = request.GET.get('q', '')  # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    print("넘어오는 값은 : ",q)
    search_sql = "SELECT 'pnum', 'pname', 'paddr', 'ptel', 'plink', 'pplace', 'pdate' FROM 'test_place' WHERE 'pplace' = %s"
    cursor.execute(search_sql,pplace)
    # if q:  # q가 있으면
        # rsearch = rsearch.filter(pplace=q) # 제목에 q가 포함되어 있는 레코드만 필터링
    return render(request, 'finalProject/riderecom1.html', {'riderecom1': rsearch, 'q': q})