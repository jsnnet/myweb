from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import cx_Oracle as oci
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

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

# def myQlist2(request):
#     conn = oci.connect('doosun/doosun@localhost:1521/xe')
#     print(conn.version)
#     cursor = conn.cursor()
#     cursor.execute('select*from test_notice')
#     nlist = cursor.fetchall()
#     # qnum, mid, qtitle, qcontent, qhit, qdate = qlist
#     # NNUM
#     # NTITLE
#     # NCONTENT
#     # NHIT
#     # NDATE
#     for (nnum, ntitle, ncontent, nhit, ndate) in nlist:
#         # print("qlist : ",qlist)
#         print("글번호: ", nnum)
#         print("제목 : ", ntitle)
#         print("조회수 : ", nhit)
#         print("작성날짜 : ", ndate)
#     return render(request, "finalProject/notice1.html", {"nlist": nlist})

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


