from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from users.models import Survey,Answer


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home1(request):
    return render(request, "users/home1.html")


def join(request):
    # if request.method == "POST":
    #     if request.POST["password1"] == request.POST["password2"]:
    #         user = User.objects.create_user(
    #             username=request.POST["username"],password=request.POST["password1"])
    #         auth.login(request,user)
    #         return redirect('home')
    #     return render(request, 'users/join.html')
    return render(request, "users/join.html")


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
    return render(request, "users/login.html")


def logout(request):
    # auth.logout(request)
    return render(request, "users/home1.html")

def qna1(request):
    return render(request, "users/qna1.html")

def notice1(request):
    return render(request, "users/notice1.html")

def ride1(request):
    return render(request, "users/ride1.html")

def race1(request):
    return render(request, "users/race1.html")

def header3(request):
    return render(request, "users/header3.html")

def footer(request):
    return render(request, "users/footer.html")

def rideintro1(request):
    return render(request, "users/rideintro1.html")

def riderecom1(request):
    return render(request, "users/riderecom1.html")

def raceintro1(request):
    return render(request, "users/raceintro1.html")

def whoiszoo1(request):
    return render(request, "users/whoiszoo1.html")

def whoispick1(request):
    return render(request, "users/whoispick1.html")

def todayzoo1(request):
    return render(request, "users/todayzoo1.html")

def countdown(request):
    return render(request, "users/countdown.html")


def survey_form(request):
    # filter 는 where 절
    # order_by 뒤에 - 표시는 : 내림차순 의미
    # [0] : 레코드 중에서 첫번째 요소 limit 0 과 같다
    survey = Survey.objects.filter(status = 'y').order_by("-survey_idx")[0]
    return render(request, "survey/survey_form.html",{"survey":survey})

# def success(request):
#     return render(request, "survey/success.html")

@csrf_exempt
def save_survey(request):
    survey_idx=request.POST["survey_idx"]
    survey_dto = Answer(survey_idx=int(request.POST["survey_idx"]),num=request.POST["num"])
    print("ans:",request.POST["ans"])
    ans= request.POST["ans"]
    survey_dto.save()
    return render(request,"survey/success.html",{"ans":ans})

def show_result(request):
    idx = request.GET['survey_idx']
    #select * from survey where survey_idx=1
    ans = Survey.objects.get(survey_idx=idx)
    answer_dto = [ans.ans1,ans.ans2,ans.ans3,ans.ans4]

    surveyList = Survey.objects.raw("""
    select survey_idx,num,count(*) sum_sum,
    round((select count(*) from survey_answer
    where survey_idx=a.survey_idx and num= a.num) * 100.0
    /(select count(*) from survey_answer where survey_idx=a.survey_idx)
    ,1) rate
    from survey_answer a where survey_idx=%s
    group by survey_idx,num
    order by num asc
    """,idx)
    surveyList = zip(surveyList,answer_dto)
    return render(request,"survey/result.html",{"surveyList":surveyList})

def show_result2(request):
    idx = request.GET['survey_idx']
    #select * from survey where survey_idx=1
    ans = Survey.objects.get(survey_idx=idx)
    answer_dto = [ans.ans1,ans.ans2,ans.ans3,ans.ans4]

    surveyList = Survey.objects.raw("""
    select survey_idx,num,count(*) sum_sum,
    round((select count(*) from survey_answer
    where survey_idx=a.survey_idx and num= a.num) * 100.0
    /(select count(*) from survey_answer where survey_idx=a.survey_idx)
    ,1) rate
    from survey_answer a where survey_idx=%s
    group by survey_idx,num
    order by num asc
    """,idx)
    surveyList = zip(surveyList,answer_dto)
    return render(request,"survey/result2.html",{"surveyList":surveyList})