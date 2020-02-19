from django.contrib.auth import authenticate
from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import auth
import cx_Oracle as oci
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import auth_login, LoginView
from django.contrib.auth.views import auth_logout
# 승마장추천 필터링을 위해 ------------
from django.shortcuts import render
from django.db.models import Q
# from .models import Document
from django.db import models
# -----------------------------------

# Create your views here.

def home1(request):
    return render(request, "finalProject/home1.html")

def join(request):
    return render(request, "finalProject/join3.html")

from .forms import LoginForm
from finalProject.models import JoinForm
from django.contrib import auth
@csrf_exempt
def join3(request):
    sign_up = JoinForm(mid=request.POST['mid'],
                   mpwd=request.POST['mpwd'],
                   mname=request.POST['mname'],
                   mtel=request.POST['mtel'],
                   madmin=request.POST['madmin']
                      )

    sign_up.save()
    return redirect('home')

def logout5(request):
    auth.logout(request)
    return redirect("home")

def login5(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        mid = request.POST["username"]
        mpwd = request.POST["password"]
        print("아이디 : ",mid)
        print("비밀번호 : ",mpwd)
        #인증함수, 로그인을 체크해주는 함수이다. 암호화가 되어서 체크해준다.
        user = auth.authenticate(username=mid, password=mpwd)
        if user is not None: # 인증완료 되었다면
            auth.login(request, user) #로그인 세션 등록
            return redirect("home")
        else: #인증 실패
            return render(request, "finalProject/join3.html", {"msg": "로그인 실패!"})
    else:
        form = LoginForm()
        return render(request, "finalProject/login5.html",{"form":form})

def join2(request):
    conn = oci.connect('doosun/doosun@localhost:1521/xe')
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
        return render(request, "finalProject/join2.html")

def login(request):

    return render(request, 'finalProject/login.html')

def login2(request):
    if request.method == "POST":
        # form = LoginForm(request.POST)
        mid = request.POST.get("mid")
        mpwd = request.POST.get("mpwd")
        # 인증함수, 로그인을 체크해주는 함수이다. 암호화가 되어서 체크해준다.
        user = auth.authenticate(mid=mid, mpwd=mpwd)
        if user is not None:  # 인증완료 되었다면
            auth.login(request, user)  # 로그인 세션 등록
            return redirect("home1")
        else:  # 인증 실패
            return render(request, "finalProject/login.html")
    else:
        return render(request, "finalProject/home1.html")

def login3(request):
    # 해당 쿠키에 값이 없을 경우 None을 return 한다.
    if request.COOKIES.get('mid') is not None:
        mid = request.COOKIES.get('mid')
        mpwd = request.COOKIES.get('mpwd')
        user = auth.authenticate(request, mid=mid, mpwd=mpwd)
        if user is not None:
            auth.login(request, user)
            return redirect("home1")
        else:
            return render(request, "login.html")

    elif request.method == "POST":
        mid = request.COOKIES.get('mid')
        mpwd = request.COOKIES.get('mpwd')
        # 해당 user가 있으면 username, 없으면 None
        user = auth.authenticate(request, mid=mid, mpwd=mpwd)

        if user is not None:
            auth.login(request, user)
            if request.POST.get("keep_login") == "TRUE":
                response = render(request, 'account/home.html')
                response.set_cookie('mid',mid)
                response.set_cookie('mpwd',mpwd)
                return response
            return redirect("home1")
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def login4(request):
    if request.method == 'POST':
        user_id = request.POST['mid']
        user_pwd = request.POST['mpwd']
        if login_verification(user_id, user_pwd):
            save_session(request, user_id, user_pwd)
            return render(request, 'finalProject/home1.html')
    return render(request,'finalProject/login.html')

def save_session(request, user_id, user_pwd):
    request.session['user_id'] = user_id
    request.session['user_pwd'] = user_pwd

def login_verification(user_id, user_pwd):
    payload = {
        'user_id' : str(user_id),
        'user_pwd' : str(user_pwd)
    }
    with requests.Session() as s:
        s.post('http://localhost:8099/finalProject/login', data = payload)
        auth = s.get('http://localhost:8099/finalProject/login4')
        if auth.status_code == 200 : # 성공적으로 가져왔을 때
            return True
        else : # 로그인 실패시
            return False


def logout(request):
    response = render(request, 'finalProject/home1.html')
    response.delete_cookie('mid')
    response.delete_cookie('mpwd')
    auth.logout(request)
    return response

def qna1(request):
    conn = oci.connect('doosun/doosun@localhost:1521/xe')
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
    conn = oci.connect('doosun/doosun@localhost:1521/xe')
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
    conn = oci.connect('doosun/doosun@localhost:1521/xe')
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
    conn = oci.connect('doosun/doosun@localhost:1521/xe')
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
    conn = oci.connect('doosun/doosun@localhost:1521/xe')
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