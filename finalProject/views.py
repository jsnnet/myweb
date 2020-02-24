from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import cx_Oracle as oci
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from .models import JoinForm
# ==============================================================================지도 api (google) 와 folium 패키지 사용
# folium 설치가 안되어 있다면 pip install 해줘야 사용가능
import folium
import googlemaps
# ==============================================================================지도 api (google) 와 folium 패키지 사용

# 승마장추천 필터링을 위해 ------------
from django.shortcuts import render
from django.db.models import Q
# from .models import Document
from django.db import models
# -----------------------------------

#--------------페이징 처리------------------------
from django.core.paginator import Paginator

#--------------페이징 처리------------------------

# 단축키 참고
# https://kgu0724.tistory.com/95

# DB 사용에 따른 conn 연결 (전역변수 사용하려면 변수 앞에 global 써주고 함수마다 변수 선언해야만 한다)
#conn = oci.connect('doosun/doosun@localhost:1521/xe')
#conn = oci.connect('doosun/doosun@192.168.0.7:1521/xe')
conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')

def home(request):
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
    if request.session.get('mid') != None:
        return render(request, 'finalProject/plzlogout.html')
    else:
        return render(request, 'finalProject/login.html')

# login 페이지에서 로그인 하면 session 에 등록
def login_session(request):
    print("html 에서 어떤 갑이 넘어오나 : ", request.POST["mid"])
    mid = request.POST["mid"]
    print("넘어온 아이디 : ", mid)
    request.session['mid'] = mid
    print("아이디 세션으로 : ", request.session['mid'])
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
    return home(request)

# 문의사항 입력
def qna(request):
    mid = request.session.get("mid")
    if (mid != None):
        return render(request, "finalProject/moon_insert.html")
    else:
        return render(request, "finalProject/login_required.html")

def qna_up(request):
    global conn; #전역변수 사용 위해
    print(conn.version)
    cursor = conn.cursor()
    mid = request.session.get("mid")
    print("mid : ", mid)
    qtitle = request.POST.get("qtitle")
    print("qtitle : ", qtitle)
    qcontent = request.POST.get("qcontent")
    print("qcontent : ", qcontent)
    # 빈칸으로 남겨두고 버튼을 눌렀을 때 알림 페이지로 이동
    if (qtitle == ''):
        return render(request, 'finalProject/none_value.html')
    elif (qcontent == '' ):
        return render(request, 'finalProject/none_value.html')
    else:
        if (mid != None):
            qtitle = request.POST.get("qtitle")
            print("qtitle : ", qtitle)
            qcontent = request.POST.get("qcontent")
            print("qcontent : ", qcontent)
            sql_insert = 'insert into question VALUES(question_seq.nextVal, :mid, :qtitle, :qcontent, :qhit, sysdate)'
            cursor.execute(sql_insert, mid=mid, qtitle=qtitle, qcontent=qcontent, qhit = 0)
            conn.commit()
            cursor.execute('select*from question')
            print(cursor.fetchall())
            cursor.close()
            conn.close
            return render(request, "finalProject/moon_insert.html")
        else:
            return render(request, "finalProject/login_required.html")

# 문의사항 출력 (추후에 내 문의로 수정할 것)
def myquestion(request):
    global conn;  # 전역변수 사용 위해
    request.session.get('mid')
    print("세션 값 : ",request.session.get('mid'))
    member_id = request.session.get('mid')
    print("세션 값 새로 저장 :",member_id)
    cursor = conn.cursor()
    myQ_sql = 'select * from question where mid =:mid'
    cursor.execute(myQ_sql, mid=member_id)
    myqlist = cursor.fetchall()
    # qnum, mid, qtitle, qcontent, qhit, qdate = myqlist
    for (qnum, mid, qtitle, qcontent, qhit, qdate) in myqlist:
        # print("qlist : ",qlist)
        print("글번호: ", qnum)
        print("qnum 타입 확인 : ",type(qnum))
        print("회원ID : ",mid)
        print("제목 : ",qtitle)
        print("조회수 : ",qhit)
        print("qhit 타입 확인 : ", type(qhit))
        print("작성날짜 : ",qdate)
        print("qdate 타입 확인 : ", type(qdate))
    return render(request, "finalProject/myQlist.html",{"myqlist":myqlist})

@csrf_exempt
def myq_view(request):
    # 내 문의 보기/수정/삭제 그리고 추가 폼으로 comm 테이블의 리스트 (문의 번호랑 회원 아이디가 FK)
    global conn;
    request.POST.get("qtitle")
    request.POST.get("qcontent")
    print(request.POST.get("qtitle"))
    print(request.POST.get("qcontent"))
    # str(request.POST.get("qnum"))
    # print("int에서 문자 : ",str(request.POST.get("qnum")))
    print("타입확인 : ", type(request.POST.get("qnum")))
    # print("qnum 확인 : ", str(request.POST.get("qnum")))
    request.session.get('mid')
    print("세션_my_qview : ", request.session.get('mid'))
    member_id = request.session.get('mid')
    print("새로 저장_my_qview :", member_id)
    cursor = conn.cursor()
    # 문의글 번호가 PK 회원아이디가 FK
    # 회원아이디는 세션으로, qnum 은 template 버튼 클릭해서 가져오기
    myq_detail = 'select * from question where mid = :mid'
    # qnum = qnum,
    # qnum = qnum,
    cursor.execute(myq_detail, mid=member_id)
    detail_view = cursor.fetchall()
    print("패치원 : ", detail_view)
    print("패치원 타입 : ", type(detail_view))
    # qnum, mid, qtitle, qcontent, qhit, qdate = detail_view
    for (qnum, mid, qtitle, qcontent, qhit, qdate) in detail_view:
        print("detail_view : ",detail_view)
        print("글번호: ", qnum)
        print("회원ID : ",mid)
        print("제목 : ",qtitle)
        print("조회수 : ",qhit)
        print("작성날짜 : ",qdate)
    return render(request, "finalProject/myQ_detail.html", {"detail_view":detail_view})

def myq_delete(request):
    # 내 문의글 상세보기에서 삭제 버튼 클릭시 여기로
    global conn;
    request.POST.get("qtitle")
    print("제목 : ",request.POST.get("qtitle"))
    request.session.get("mid")
    print("아이디 : ",request.session.get("mid"))
    del_myq = 'delete from question where mid = :mid and qtitle = :qtitle'
    return render(request, "finalProject/myQ_delete.html")

# 공지사항 불러오기
# sysdate 로 생성된 qdate 값이 return 으로 넘어가지 않음
def notice1(request):
    global conn;  # 전역변수 사용 위해
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from notice')
    # cursor.execute('select nnum, ntitle, ncontent, nhit, to_char(ndate) from notice')
    # print("공지 제목 날짜 : ",res)
    nlist = cursor.fetchall()
    # for (nnum, ntitle, ncontent, nhit, ndate) in nlist:
    #     # print("qlist : ",qlist)
    #     print("글번호: ", nnum)
    #     print("제목 : ", ntitle)
    #     print("내용 : ", ncontent)
    #     print("조회수 : ", nhit)
    #     print("작성날짜 : ", ndate)
    # for (ntitle, ndate) in nlist:
    #     print("qlist : ",qlist)
    #     print("글번호: ", nnum)
    #     print("제목 : ", ntitle)
    #     print("내용 : ", ncontent)
    #     print("조회수 : ", nhit)
    #     print("작성날짜 : ", ndate)
    return render(request, "finalProject/notice_gogzy.html", {"nlist": nlist})

def up_review(request):
    global conn;
    cursor = conn.cursor()
    mid = request.session.get("mid")
    if (mid != None):
        cursor.close()
        conn.close
        return render(request, 'finalProject/review_upload.html')
    else:
        return render(request, 'finalProject/login_required.html')

def write_review2(request):
    global conn; #전역변수 사용 위해
    mid = request.session.get("mid")
    print(conn.version)
    cursor = conn.cursor()
    retitle = request.POST.get("retitle")
    print("retitle : ", retitle)
    recontent = request.POST.get("recontent")
    print("qcontent : ", recontent)
    print("mid 있는지 : ",mid)
    # 빈칸으로 남겨두고 버튼을 눌렀을 때 알림 페이지로 이동
    if (retitle == ''):
        return render(request, 'finalProject/none_value.html')
    elif (recontent == ''):
        return render(request, 'finalProject/none_value.html')
    else:
        if (mid != None):
            sql_insert = 'insert into review VALUES(review_seq.nextVal, :retitle, :recontent, :rehit, sysdate)'
            cursor.execute(sql_insert, retitle=retitle, recontent=recontent, rehit = 0)
            conn.commit()
            cursor.execute('select*from review')
            print(cursor.fetchall())
            cursor.close()
            conn.close
            return render(request, "finalProject/review_upload.html")
        else:
            return render(request, 'finalProject/login_required.html')

# 승마장 추천
def riderecom1(request):
    global conn;  # 전역변수 사용 위해
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
    global conn;  # 전역변수 사용 위해
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from place')
    return render(request, 'finalProject/sungma_chu.html.html') #{'riderecom2': rsearch, 'q': q} #riderecom2.html 이었던 것

# 승마체험장 추천에서 checkbox 사용 하는 함수
def rideSearch(request):
    global conn;  # 전역변수 사용 위해
    request.POST.getlist('chk_pplace')
    chk_slct = request.POST.get('chk_pplace')
    print(chk_slct)
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

def footer(request):
    return render(request, "finalProject/footer.html")

def rideintro1(request):
    global conn;  # 전역변수 사용 위해
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

    map_ori = folium.Map(location=[37.479833, 126.880097], zoom_start=17)
    folium.Marker([37.479833, 126.880097], popup='<b>가산</b>').add_to(map_ori)
    map_ori.save('finalProject/sungma_cheso.html')

    return render(request, "finalProject/sungma_cheso.html", {'plist':plist})

def rideintro2(request):
    # gkey = "AIzaSyDAbziSH8lb_794Kdf9VZSl5CIwMR2ImUI"
    # gmaps = googlemaps.client(key=gkey)
    # gmaps.geocode('대한민국 서울특별시 송파구 오륜동 올림픽로 424', language = 'ko')
    # map_ori = folium.Map(location=[37.479833, 126.880097], zoom_start=17)
    # folium.Marker([37.479833, 126.880097], popup='<b>가산</b>').add_to(map_ori)
    # map_ori.save('finalProject/map1.html')
    return render(request, "finalProject/map3.html")

def raceintro1(request):
    return render(request, "finalProject/gyungma_jangso.html")

def whoiszoo1(request):
    return render(request, "finalProject/whois_juingong.html")

def whoispick1(request):
    return render(request, "finalProject/whois_onepick.html")

def todayzoo1(request):
    return render(request, "finalProject/today_juingong.html")

def countdown(request):
    return render(request, "finalProject/countdown.html")

def review(request):
    global conn;  # 전역변수 사용 위해
    cursor = conn.cursor()
    cursor.execute('select*from review')
    rlist = cursor.fetchall
    return render(request, "finalProject/review.html", {"rlist":rlist})

def index(request):
    global conn;  # 전역변수 사용 위해
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
# def home(request):
#     global conn;  # 전역변수 사용 위해
#     print(conn.version)
#     cursor = conn.cursor()
#     nlist = cursor.execute('select*from notice')
#     print("오브젝트냐 리스트냐 : ",nlist) # 리스트여야 한다
#     notice_list = list(nlist)
#     print("최종 자료형은? : ",type(notice_list))
#     # 블로그 모든 글을 대상으로
#     # 블로그 모든 객체를 세개 단위를 한 페이지로 자르기
#     paginator = Paginator(notice_list, 3)
#     # request 된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
#     page = request.GET.get('page')
#     # request 된 페이지를 얻어온 뒤 return 해준다.
#     posts = paginator.get_page(page) # 에러 : object of type 'cx_Oracle.Cursor' has no len()
#     # posts 에는 요청된 페이지가 담겨있으니까, 얘를 return 해주자.
#     return render(request, 'finalProject/test.html', {'nlist':nlist, 'posts': posts})


        # return render(request, "finalProject/join_gaip.html")