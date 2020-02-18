from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import auth
import cx_Oracle as oci
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import auth_login, LoginView
from django.contrib.auth.views import auth_logout


# Create your views here.

def home1(request):
    return render(request, "finalProject/home1.html")

def join(request):
    return render(request, "finalProject/join2.html")

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

class UserLoginView(LoginView):           # 로그인
    template_name = 'user/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)

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
    return render(request, "finalProject/riderecom1.html")

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


