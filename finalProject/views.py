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

#--------------페이징 처리------------------------
from django.core.paginator import Paginator

#--------------페이징 처리------------------------


def home1(request):
    return render(request, "finalProject/home_main.html")

def join(request):
    return render(request, "finalProject/join_gaip.html")

# (상) sqlite 과 oracle DB에 동시 회원가입하는 부분====================================
from .forms import LoginForm,UserForm
from django.contrib import auth
@csrf_exempt
def join_Oraclite(request):
    # 폼 안쓰고 새로 생성한 모델 활용 ==================================================================================
    sign_up = JoinForm(mid=request.POST['mid'],
                   mpwd=request.POST['mpwd'],
                   mname=request.POST['mname'],
                   mtel=request.POST['mtel'],
                   madmin=request.POST['madmin']
                      )
    sign_up.save()
    # ================================================================================================================
    # sqlite 에 회원가입 완료
    # oracle 에 회원 가입 시작
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute("select*from member")
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
        join_insert = "insert into member VALUES(member_seq.nextVal, :mid, :mpwd, :mname, :mtel, :madmin, sysdate)"
        cursor.execute(join_insert, mid=mid, mpwd=mpwd, mname=mname, mtel=mtel, madmin=madmin)
        cursor.close()
        conn.commit()
        conn.close()
        return render(request, "finalProject/home_main.html")
    else:
        return render(request, "finalProject/join_gaip.html")
    return redirect('home')
# (하) sqlite 과 oracle DB에 동시 회원가입하는 부분==============================================================================

# 홈에서 로그인 글씨 누르면 login 페이지로 이동
def login(request):
    return render(request, 'finalProject/login.html')

# login 페이지에서 로그인 하면 session 에 등록
def login_session(request):
    print("html 에서 어떤 갑이 넘어오나 : ", request.POST["mid"])
    mid = request.POST["mid"]
    print("넘어온 아이디 : ", mid)
    request.session['id'] = mid
    print("아이디 세션으로 : ", request.session['id'])
    # 비밀번호 테스트용
    # request.session['password'] = ' '
    # return HttpResponse("finalProject/home_main.html")
    return render(request, "finalProject/home_main.html")

# session 확인하기 위한 함수
# def access_session(request):
#     response = "<h1>Welcome to Sessions of dataflair</h1><br>"
#     if request.session.get('id'):
#         response += "Name : {0} <br>".format(request.session.get('id'))
#         return HttpResponse(response)
#     else:
#         return redirect('login_session')

# 로그아웃
def logout(request):
    response = render(request, 'finalProject/home_main.html')
    response.delete_cookie('mid')
    response.delete_cookie('mpwd')
    auth.logout(request)
    return response

# 문의사항 입력
def qna1(request):
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from member')
    print(cursor.fetchone())
    mid = request.POST.get("mid")
    print("mid : ", mid)
    qtitle = request.POST.get("qtitle")
    print("qtitle : ", qtitle)
    qcontent = request.POST.get("qcontent")
    print("qcontent : ", qcontent)
    if (mid != None):
        sql_insert = 'insert into question VALUES(question_seq.nextVal, :mid, :qtitle, :qcontent, :qhit, sysdate)'
        cursor.execute(sql_insert, mid=mid, qtitle=qtitle, qcontent=qcontent, qhit = 0)
        conn.commit()
        cursor.execute('select*from question')
        print(cursor.fetchall())
        cursor.close()
        conn.close
        return render(request, "finalProject/moon_insert.html")
    else:
        return render(request, "finalProject/moon_insert.html")

# 문의사항 출력 (추후에 내 문의로 수정할 것)
def myquestion(request):
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from question')
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

# 공지사항 불러오기
def notice1(request):
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from notice')
    nlist = cursor.fetchall()

    for (nnum, ntitle, ncontent, nhit, ndate) in nlist:
        # print("qlist : ",qlist)
        print("글번호: ", nnum)
        print("제목 : ", ntitle)
        print("내용 : ", ncontent)
        print("조회수 : ", nhit)
        print("작성날짜 : ", ndate)
    return render(request, "finalProject/notice_gogzy.html", {"nlist": nlist})

# 승마장 추천
def riderecom1(request):
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from place')
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
    return render(request, "finalProject/sungma_chu.html", {"plist": plist})

# 승마장 추천 필터링 하려는 테스트
def recom_list(request):
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from place')
    return render(request, 'finalProject/sungma_chu.html.html') #{'riderecom2': rsearch, 'q': q} #riderecom2.html 이었던 것

# 승마체험장 추천에서 checkbox 사용 하는 함수
def rideSearch(request):
    request.POST.getlist('chk_pplace')
    chk_slct = request.POST.get('chk_pplace')
    print(chk_slct)
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print("버젼 확인 :",conn.version)
    cursor = conn.cursor()
    # clob 데이터 타입은 char 로 바꿔서 바인딩 해야 한다 https://www.warevalley.com/support/orange_view.asp?page=30&num=11943
    sql_chk = 'select * from place where to_char(pplace) =:pplace'
    # where to_char(clob_column) = :clob_column
    cursor.execute(sql_chk, pplace=chk_slct)
    # res1 = cursor.execute(sql_chk, pplace=chk_slct)
    res2 = cursor.fetchall()
    print("selelct where 쓴 결과 : ",res2) # fechall 괄호 안쓰면 object 로 넘어온다
    for (pnum, pname, paddr, ptel, plink, pplace, pdate) in res2:
        print("승마장 번호: ", pnum)
        print("승마장 이름 : ", pname)
        print("주소 : ", paddr)
        print("연락처 : ", ptel)
        print("링크 : ", plink)
        print("부대시설 : ", pplace)
        print("등록날짜 : ", pdate)

    return render(request, 'finalProject/sungma_radio1.html',{"res2": res2})  #, {'srch': srch, 'w': w}

def ride1(request):
    return render(request, "finalProject/sungma_sogae.html")

def race1(request):
    return render(request, "finalProject/gyungma_sogae.html")

def header3(request):
    return render(request, "finalProject/header3.html")

def footer(request):
    return render(request, "finalProject/footer.html")

def rideintro1(request):
    return render(request, "finalProject/rideintro1.html")

def raceintro1(request):
    return render(request, "finalProject/raceintro1.html")

def whoiszoo1(request):
    return render(request, "finalProject/whois_juingong.html")

def whoispick1(request):
    return render(request, "finalProject/whois_onepick.html")

def todayzoo1(request):
    return render(request, "finalProject/today_juingong.html")

def countdown(request):
    return render(request, "finalProject/countdown.html")

def review(request):
    return render(request, "finalProject/review.html")

def index(request):
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from notice')
    nlist = cursor.fetchall()
    # posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(nlist, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    page_range = 5 #페이지 범위 지정 예 1, 2, 3, 4, 5 / 6, 7, 8, 9, 10
    current_block = math.ceil(int(page)/page_range) #해당 페이지가 몇번째 블럭인가
    start_block = (current_block-1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]
    return render(request, 'finalProject/test.html', {
        'contacts': contacts,
        'p_range' : p_range,
    })

# https://egg-money.tistory.com/111?category=811218
# https://egg-money.tistory.com/111?category=811218 # detail 이란 함수에 관한 에러 때문에
def home(request):
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    nlist = cursor.execute('select*from notice')
    print("오브젝트냐 리스트냐 : ",nlist) # 리스트여야 한다
    notice_list = list(nlist)
    print("최종 자료형은? : ",type(notice_list))
    # 블로그 모든 글을 대상으로
    # 블로그 모든 객체를 세개 단위를 한 페이지로 자르기
    paginator = Paginator(notice_list, 3)
    # request 된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request 된 페이지를 얻어온 뒤 return 해준다.
    posts = paginator.get_page(page) # 에러 : object of type 'cx_Oracle.Cursor' has no len()
    # posts 에는 요청된 페이지가 담겨있으니까, 얘를 return 해주자.
    return render(request, 'finalProject/test.html', {'nlist':nlist, 'posts': posts})

# -------------------------------------------------------------------------------------------로그인 안하면 접근 못하도록
# https://jupiny.com/2017/11/25/step-by-step-page-using-django-session/
from django.views import View
from django.shortcuts import redirect, render
# from django.core.urlresolver import reverse
from django.core.exceptions import PermissionDenied

class Step1View(View):

    def get(self, request, *args, **kwargs):
        request.session['step1_complete'] = False
        request.session['step2_complete'] = False
        return render(request, 'step1.html')

    def post(self, request, *args, **kwargs):
        request.session['step1_complete'] = True
        return redirect(reverse('step2'))


class Step2View(View):

    def get(self, request, *args, **kwargs):
        if not request.session.get('step1_complete', False):
            raise PermissionDenied
        request.session['step1_complete'] = False
        return render(request, 'step2.html')

    def post(self, request, *args, **kwargs):
        request.session['step2_complete'] = True
        return redirect(reverse('step3'))


class Step3View(View):

    def get(self, request, *args, **kwargs):
        if not request.session.get('step2_complete', False):
            raise PermissionDenied
        request.session['step2_complete'] = False
        return render(request, 'step3.html')

# -------------------------------------------------------------------------------------------로그인 안하면 접근 못하도록