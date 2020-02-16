from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from survey.models import Survey,Answer
# Create your views here.



def home(request):
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