from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import cx_Oracle as oci


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home1(request):
    return render(request, "finalProject/home1.html")


def join(request):
    # if request.method == "POST":
    #     if request.POST["password1"] == request.POST["password2"]:
    #         user = User.objects.create_user(
    #             username=request.POST["username"],password=request.POST["password1"])
    #         auth.login(request,user)
    #         return redirect('home')
    #     return render(request, 'finalProject/join.html')
    return render(request, "finalProject/join.html")


def login(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(request, username=username, password=password)
    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect('home')
    #     else:
    #         return render(request, 'login.html', {'error': 'username or password is incorrect'})
    # else:
    return render(request, "finalProject/login.html")


def logout(request):
    # auth.logout(request)
    return render(request, "finalProject/home1.html")

def qna1(request):
    conn = oci.connect('doosun/doosun@localhost:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from test_member')
    # id로 검색
    # sql_select_by_id = 'select * from test_member where id = :mid'
    # cursor = conn.cursor()
    # cursor.execute(sql_select_by_id, mid='admin')
    print(cursor.fetchone())
    # insert
    # sql_insert = 'insert into test_member VALUES(test_member_seq.nextVal, :id, :password, :email)'
    # cursor.execute(sql_insert, id='kosmo3', password='kosmo31234', email='kosmo3@ikosmo.com')
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
    # insert한 내용을 commit
    # cursor.execute('select*from test_question')
    # print(cursor.fetchall())
    # cursor.close()
    # conn.close
    # return render(request, "finalProject/qna1.html")

def myquestion(request):
    conn = oci.connect('doosun/doosun@localhost:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    # idm = request.GET['mid']
    # myq = request.POST.get("mid")
    # qlist_dto = [myq.qnum,myq.mid,myq.qtitle,myq.qcontent,myq.qhit,myq.qdate]
    # idQlist = cursor.execute('select*from test_question where mid = idm')
    # idQlist = zip(idQlist,qlist_dto)
    # return render(request, "finalProject/myQlist2.html", {"idQlist": idQlist})
    cursor.execute('select*from test_question')
    # select 된 값들이 잘 보여지는지 출력
    # print("fecth : ", cursor.fetchall())
    # print(cursor.fetchall())
    # 여기선 확인용/ 여기말고 myQlist.html에서 사용하기
    #qlist = cursor.fetchall()
    #print(cursor.fetchall())
    #qnum, mid, qtitle, qcontent, qhit, qdate = qlist
    #return render(request, "finalProject/myQlist2.html")  #, {"qlist":qlist} ,
    qlist = cursor.fetchall()
    # qnum, mid, qtitle, qcontent, qhit, qdate = qlist
    for (qnum, mid, qtitle, qcontent, qhit, qdate) in qlist:
        print("qlist : ",qlist)
        # print("글번호: ", qnum)
        # print("회원ID : ",mid)
        # print("제목 : ",qtitle)
        # print("조회수 : ",qhit)
        # print("작성날짜 : ",qdate)

    # for e in cursor.fetchall():
    #     print("e"," : ",e)
        # qnum, mid, qtitle, qcontent, qhit, qdate = e
        # print("글번호: ",qnum)
        # print("회원ID : ",mid)
        # print("제목 : ",qtitle)
        # print("조회수 : ",qhit)
        # print("작성날짜 : ",qdate)
    return render(request, "finalProject/myQlist.html")
    # {"qnum":qnum,"mid":mid,"qtitle":qtitle,"qhit":qhit,"qdate":qdate}

    # cursor.fetchall()
    # qnum = request.POST.get("qnum")
    # # print("qnum : ", qnum)
    # mid = request.POST.get("mid")
    # qtitle = request.POST.get("qtitle")
    # qhit = request.POST.get("qhit")
    # qdate = request.POST.get("qdate")
    # return render(request, "finalProject/myquestion.html")

def myquestion2(request):
    conn = oci.connect('doosun/doosun@localhost:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    #cursor.execute('select*from test_question')
    sql_select = "select qnum,mid,qtitle,qhit,to_char(qdate,'yyyy-mm-dd')\
            qdate from test_question order by 1 desc"
    cursor.execute(sql_select)
    selectlists = myquestion2()
    for row in selectlists:
        stv = list(row)  # 튜플을 리스트로 변환
        str1 = ''.join(str(e) for e in stv)  # 리스트로부터 하나씩 인자를 뽑아서 문자열로 변환
        print(str1)
    cursor.close()
    conn.close()
    return render(request, "finalProject/myQlist.html")
    # {"qnum":qnum,"mid":mid,"qtitle":qtitle,"qhit":qhit,"qdate":qdate}

def myQlist2(request):
    return render(request, "finalProject/myQlist2.html")

def notice1(request):
    return render(request, "finalProject/notice1.html")

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


