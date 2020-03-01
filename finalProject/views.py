# 분석을 위한 import #################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import missingno as msno
import csv
import tensorflow as tf
from PIL import Image
import os, glob, numpy as np

# keras 모델을 읽어오기 위한 keras 모델
from pandas import read_csv
from tensorflow.python.keras.models import load_model
from keras.models import model_from_json
import scipy.stats as stats
import matplotlib.pyplot as plt
# 분석을 위한 import #################################################################

from django.shortcuts import render, redirect
import cx_Oracle as oci
from django.views.decorators.csrf import csrf_exempt
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

########## 캐시 처리 ###########################################
from django.core.cache import caches
from django.core.cache import cache
########## 캐시 처리 ###########################################

# 인기 마 선택 (Survey와 똑같이) #############
from django.http import HttpResponse
from finalProject.models import MyPick,Horse
#############################################


# 단축키 참고
# https://kgu0724.tistory.com/95

# DB 사용에 따른 conn 연결 (전역변수 사용하려면 변수 앞에 global 써주고 함수마다 변수 선언해야만 한다)
conn = oci.connect('doosun/doosun@localhost:1521/xe')
# conn = oci.connect('doosun/doosun@192.168.0.7:1521/xe')
# conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')

########################################### 작성해야 할 아래에 있던 코드 위로 올려 놓음 ############################################################################

# 경마 누가 주인공이냐
def whoiszoo1(request):
    # csv 파일 경로에 따른 아래와 같은 표현
    # 주피터로 테스트한 함수들 차례로 하위 함수 개념으로 전부 붙여넣음
    # 주피터에서 함수 실행하던 것을은 필요하면 print() 메서드 안에 넣어서 출력해 볼 수 있음
    HorScoP8 = 'horsedata.csv'
    HorScoP8 = pd.read_csv(HorScoP8)
    # df = read_csv(HorScoP8)
    df1 = pd.DataFrame(HorScoP8)
    # print(df1)
    del df1['Unnamed: 0']
    # print("df1 : ",df1)

    def sexage(hname, gmeter):
        data = df1[(df1['마명'] == hname)]
        sex = data['성별'].iloc[0]
        rrange = df1['나이'].max()

        # 나이 범위만큼 age 리스트를 만들고 각 나이의 수를 저장
        # std 리스트를 생성하고 해당 경기와 같은 경주거리의 기록 데이터를 저장
        age = [0 for i in range(rrange)]
        agesum = 0
        std_list = []
        for i in range(len(df1)):
            if df1.loc[i, '거리'] == gmeter:
                std_list.append(df1.loc[i, '새기록'])
            for j in range(rrange):
                if df1.loc[i, '성별'] == sex:
                    if df1.loc[i, '나이'] == j + 1:
                        age[j] = age[j] + 1
                        agesum = agesum + 1

        # age 리스트 범위만큼 weight 리스트를 만들고 가중치를 저장
        weight = [0 for i in range(rrange)]
        for i in range(len(age)):
            weight[i] = age[i] / agesum

        # 가중치를 재조정하고 예측값을 저장
        std = float(np.std(std_list))
        readjust = []
        for i in weight:
            readjust.append(i * std)

        # 해당 말의 나이에 해당하는 예측값을 반환
        horseage = int(data['나이'].iloc[0])
        sexage = readjust[horseage - 1]

        return sexage

    # 경기 거리와 거리별 속도를 분석하여 예측값을 반환
    def meterspeed(hname, gmeter):
        data = df1[(df1['마명'] == hname)].index

        # 해당 마명의 해당 경기 거리
        s1 = []
        g3 = []
        g1 = []
        record = []
        for i in data:
            if df1.loc[i, '거리'] == gmeter:
                s1.append(df1.loc[i, 'S1화롱'])
                g3.append(df1.loc[i, 'G3화롱'])
                g1.append(df1.loc[i, 'G1화롱'])
                record.append(df1.loc[i, '새기록'])

        # 각 화롱의 순간속도와 경주기록의 상관관계(기울기) 분석 및 가중치 부여
        s1_slope, s1_intercept, s1_r_value, s1_p_value, s1_stderr = stats.linregress(s1, record)
        g3_slope, g3_intercept, g3_r_value, g3_p_value, g3_stderr = stats.linregress(g3, record)
        g1_slope, g1_intercept, g1_r_value, g1_p_value, g1_stderr = stats.linregress(g1, record)
        slope_list = [s1_slope, g3_slope, g1_slope]
        slope_weight = [0 for i in range(len(slope_list))]
        slope_total = 0
        for i in range(len(slope_list)):
            slope_total = slope_total + slope_list[i]
        for i in range(len(slope_list)):
            slope_weight[i] = float(slope_list[i] / slope_total)

        # 화롱의 표준편차에 가중치를 부여한 예측값 반환
        std_s1 = float(np.std(s1)) * slope_weight[0]
        std_g3 = float(np.std(g3)) * slope_weight[1]
        std_g1 = float(np.std(g1)) * slope_weight[2]
        meterspeed = (std_s1 + std_g3 + std_g1)

        return meterspeed

    # 습도와 기록의 상관관계를 분석하여 예측값을 반환
    def humidity(hname, humidity):
        data = df1[(df1['마명'] == hname)].index

        # 습도와 기록의 상관관계 분석
        humi_list = []
        record_list = []
        for i in range(len(df1)):
            humi_list.append(df1.loc[i, '습도'])
            record_list.append(df1.loc[i, '새기록'])
        slope, intercept, r_value, p_value, stderr = stats.linregress(humi_list, record_list)

        # 당해 경주마, 습도에 해당하는 새기록의 표준편차 계산
        std_list = []
        for i in data:
            if df1.loc[i, '습도'] == humidity:
                std_list.append(df1.loc[i, '새기록'])
        std = float(np.std(std_list))

        # 표준편차와 상관관계값 연산
        humidity = std * slope

        return humidity

    # 기수와 기록의 상관관계를 분석하여 예측값을 반환
    def rider(hname, gmeter, human):
        data = df1[(df1['마명'] == hname) & (df1['거리'] == gmeter)].index
        data_list = list(data)

        # 기수 이름 데이터 정리
        human_list = []
        record_list = []
        for i in range(len(data)):
            human_list.append(df1.loc[i, '기수'])
            record_list.append(df1.loc[i, '새기록'])
        human_set = set(human_list)
        set_list = list(human_set)

        # 기수 이름에 따른 기록 중위값 리스트 작성
        mean_list = []
        for i in range(len(set_list)):
            temp = []
            for j in range(len(data_list)):
                if df1.loc[j, '기수'] == set_list[i]:
                    temp.append(df1.loc[j, '새기록'])
            median = np.mean(temp)
            mean_list.append(median)

        # 중위값을 정렬하고 회귀도 분석
        index_list = [i + 1 for i in range(len(mean_list))]
        median_list = sorted(mean_list)
        slope, intercept, r_value, p_value, stderr = stats.linregress(index_list, median_list)

        # 당해 경주마, 기수에 해당하는 새기록의 표준편차 계산
        std_list = []
        for i in data:
            if df1.loc[i, '기수'] == human:
                std_list.append(df1.loc[i, '새기록'])
        std = float(np.std(std_list))

        # 표준편차와 상관관계값 연산
        rider = std * slope

        return rider

    def predict(hname):

        ## 임의로 값을 주입함
        ## 해당 값들을 select 문으로 받아와야 함 ###################################################################

        # gmeter 는 경기 테이블 game
        # humi 는 어디에?
        # human 은 기수 테이블 rider

        gmeter = 800
        humi = 6
        human = '문현진'
        ## 임의로 값을 주입함

        data = df1[(df1['마명'] == hname) & (df1['거리'] == gmeter)]
        median = data['새기록'].mean()

        # 해당 경주마의 기록 추세 계산
        hdata = df1[(df1['마명'] == hname)].index
        hdata_list = list(hdata)
        new_record = []
        for i in hdata_list:
            new_record.append(df1.loc[i, '새기록'])
        slope, intercept, r_value, p_value, stderr = stats.linregress(hdata_list, new_record)

        # def sexage 메서드 실행
        sexage_predict = sexage(hname, gmeter)
        if np.isnan(sexage_predict) == True:
            sexage_predict = 0
        # def meterspeed 메서드 실행
        meterspeed_predict = meterspeed(hname, gmeter)
        if np.isnan(meterspeed_predict) == True:
            meterspeed_predict = 0
        # def humidity 메서드 실행
        humidity_predict = humidity(hname, humi)
        if np.isnan(humidity_predict) == True:
            humidity_predict = 0
        # def rider 메서드 실행
        rider_predict = rider(hname, gmeter, human)
        if np.isnan(rider_predict) == True:
            rider_predict = 0

        # 예측값 데이터를 합하고 기록 추세를 가중치로 부여함
        sum_predict = sexage_predict + meterspeed_predict + humidity_predict + rider_predict
        pre_data = sum_predict * slope
        predict = 0
        if slope >= 0:
            predict = median + pre_data
        else:
            predict = median - pre_data

        return predict

    # 메인 메서드
    def main():
        hname_list = ['개선문', '오라스타', '아라신화', '삼다지존', '승일교', '행복의문', '태산여왕', '만점왕']

        # 마명에 해당하는 예측값을 반환
        record_list = []
        for i in hname_list:
            prenum = round(predict(i), 2)
            record_list.append(prenum)

        # 마명에 해당하는 예측값을 딕셔너리 형태로 담아 오름차순으로 정렬
        hzip = zip(hname_list, record_list)
        hdict = dict(hzip)
        res = sorted(hdict.items(), key=(lambda x: x[1]))

        # 예측된 1, 2등마의 데이터를 반환
        first_horse = res[0]
        second_horse = res[1]
        horse = [first_horse, second_horse]

        return horse
    print("여기까진?")
    print("최종결과 : ", main())
    predict_list = main()
    return render(request, "finalProject/whois_juingong.html", {"predict_list":predict_list})

# 경마 누가 주인공인지 인기투표
def whoispick1(request):
    # 경기마 테이블 horse select 로 가져와서 목록 보여주기
    # global conn
    # cursor_select = conn.cursor()
    # hselect_sql = 'select * from horse'
    # cursor_select.execute(hselect_sql)
    # hlist = cursor_select.fetchall()
    ######### 여기부터 Survey 에서 가져온 것 #####################################
    # filter 는 where 절
    # order_by 뒤에 - 표시는 : 내림차순 의미
    # [0] : 레코드 중에서 첫번째 요소 limit 0 과 같다
    survey = MyPick.objects.filter(status='y').order_by("-survey_idx")[0]
    return render(request, "finalProject/whois_onepick.html", {"survey":survey})

@csrf_exempt
def save_survey(request):
    survey_idx=request.POST["survey_idx"]
    survey_dto = Horse(survey_idx=int(request.POST["survey_idx"]),num=request.POST["num"])
    print("ans:",request.POST["ans"])
    ans= request.POST["ans"]
    survey_dto.save()
    return render(request,"finalProject/success.html",{"ans":ans})

def show_result(request):
    idx = request.GET['survey_idx']
    #select * from  where survey_idx=1
    ans = MyPick.objects.get(survey_idx=idx)
    answer_dto = [ans.ans1,ans.ans2,ans.ans3,ans.ans4,ans.ans5,ans.ans6,ans.ans7,ans.ans8,ans.ans9,ans.ans10,
                  ans.ans11,ans.ans12,ans.ans13,ans.ans14,ans.ans15,ans.ans16,ans.ans17,ans.ans18,ans.ans19,ans.ans20,
                  ans.ans21,ans.ans22,ans.ans23,ans.ans24,ans.ans25,ans.ans26,ans.ans27,ans.ans28,ans.ans29,ans.ans30,
                  ans.ans31,ans.ans32,ans.ans33,ans.ans34,ans.ans35,ans.ans36,ans.ans37,ans.ans38,ans.ans39,ans.ans40,
                  ans.ans41,ans.ans42,ans.ans43,ans.ans44,ans.ans45,ans.ans46,ans.ans47,ans.ans48,ans.ans49,ans.ans50,
                  ans.ans51,ans.ans52,ans.ans53,ans.ans54,ans.ans55, ans.ans56, ans.ans57, ans.ans58, ans.ans59,ans.ans60,
                  ans.ans61, ans.ans62, ans.ans63, ans.ans64, ans.ans65, ans.ans66, ans.ans67, ans.ans68, ans.ans69,
                  ans.ans70,ans.ans71,ans.ans72,ans.ans73,ans.ans74,ans.ans75,ans.ans76,ans.ans77,ans.ans78]

    surveyList = MyPick.objects.raw("""
    select survey_idx,num,count(*) sum_sum,
    round((select count(*) from finalProject_horse
    where survey_idx=a.survey_idx and num= a.num) * 100.0
    /(select count(*) from finalProject_horse where survey_idx=a.survey_idx)
    ,1) rate
    from finalProject_horse a where survey_idx=%s
    group by survey_idx,num
    order by num asc
    """, idx)
    print("surveyList : ", surveyList)
    surveyList = zip(surveyList,answer_dto)
    print("surveyList 타입 : ", type(surveyList))
    return render(request, "finalProject/whois_onepick_result5.html", {"surveyList":surveyList})

# 오늘의 주인공은?
def todayzoo1(request):
    # return render(request, "finalProject/today_juingong.html")
    return render(request, "finalProject/whois_onepick_result5.html")


def home(request):
    return render(request, "finalProject/home_main.html")

def join(request):
    return render(request, "finalProject/join_gaip3.html")

####################################################################### (상) sqlite 과 oracle DB에 동시 회원가입하는 부분
from django.contrib import auth
@csrf_exempt
def join_Oraclite(request):
    global conn;
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
        conn.commit()
        # cursor.close()
        # conn.close
        return render(request, "finalProject/home_main.html")
    else:
        return render(request, "finalProject/join_gaip.html")
    return redirect('home')
####################################################################### (하) sqlite 과 oracle DB에 동시 회원가입하는 부분

# 홈에서 로그인 글씨 누르면 login 페이지로 이동
def login(request):
    if request.session.get('mid') != None:
        return render(request, 'finalProject/plzlogout.html')
    else:
        return render(request, 'finalProject/login1.html')

# login 페이지에서 로그인 하면 session 에 등록
# DB에 등록된 아이디와는 비교 기능 미구현
def login_session(request):
    print("html 에서 어떤 갑이 넘어오나 : ", request.POST["mid"])
    mid = request.POST["mid"]
    print("넘어온 아이디 : ", mid)
    mpwd_pass = request.POST.get("mpwd")
    print("패스워드 값 mpwd : ", mpwd_pass)
    # 회원가입한 회원의 아이디/비밀번호를 사용, DB에 존재하는지에 따라 로그인 승인
    if mpwd_pass is None:
        return render(request, 'finalProject/none_value.html')
    else:
        global conn;
        print("첫if mpwd_pass : ", mpwd_pass)
        cursor = conn.cursor()
        pwd_chk = 'select * from member where mid = :mid'
        cursor.execute(pwd_chk, mid=mid)
        chk_member = cursor.fetchall()
        chk_pwd = None
        print("선언한 chk_pwd : ", chk_pwd)
        print("for문 들어가기 전 mpwd_pass : ", mpwd_pass)
        for (mnum, mid, mpwd, mname, mtel, madmin, mdate) in chk_member:
            print("가입된 패스워드 : ", mpwd)
            chk_pwd = mpwd
            print("chk_pwd : ", chk_pwd)
        if mpwd_pass != chk_pwd:
            print("if 진입한 mpwd : ", mpwd_pass)
            print("if 진입한 chk_pqd : ", chk_pwd)
            return render(request, 'finalProject/login_required.html')
        else:
            request.session['mid'] = mid
            print("아이디 세션으로 : ", request.session['mid'])
            # 비밀번호 테스트용
            # request.session['password'] = ' '
            # return HttpResponse("finalProject/home_main.html")
            # conn.commit()
            # conn.close()
            return render(request, "finalProject/home_main.html")

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
        return render(request, "finalProject/myQ_insert.html")
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
            # cursor.close()
            # conn.close
            return render(request, "finalProject/myQ_insert.html")
        else:
            return render(request, "finalProject/login_required.html")

# 문의사항 출력 (추후에 내 문의로 수정할 것)
def myquestion(request):
    global conn;  # 전역변수 사용 위해
    request.session.get('mid')
    print("세션 값 : ",request.session.get('mid'))
    member_id = request.session.get('mid')
    print("세션 값 새로 저장 :", member_id)
    cursor = conn.cursor()
    myQ_sql = 'select * from question where mid =:mid'
    cursor.execute(myQ_sql, mid=member_id)
    conn.commit()
    myqlist = cursor.fetchall()
    # cursor.close()
    # conn.close
    return render(request, "finalProject/myQlist.html",{"myqlist":myqlist})

@csrf_exempt
def myq_view(request):
    # 내 문의 보기/수정/삭제 그리고 추가 폼으로 comm 테이블의 리스트 (문의 번호랑 회원 아이디가 FK)
    global conn;
    # 문의 리스트에서 클릭한 문의만 가져오고 싶을때
    # 해당 문의의 문의 번호를 가져온다
    qnum = request.GET["qnum"]
    print("qnum : ", qnum)
    # 로그인 아이디 세션 가져오기
    member_id = request.session.get('mid')
    cursor_myq = conn.cursor()
    cursor_comm = conn.cursor()
    # 문의글 번호가 PK 회원아이디가 FK
    # 회원아이디는 세션으로, qnum 은 template 버튼 클릭해서 가져오기
    myq_detail = 'select * from question where qnum = :qnum'
    # 댓글 테이블에서 qnum 으로 해당 글 댓글 불러오기
    comm_sql = 'select * from comm where qnum = :qnum'
    cursor_myq.execute(myq_detail, qnum=qnum)
    cursor_comm.execute(comm_sql, qnum=qnum)
    conn.commit()
    detail_view = cursor_myq.fetchall()
    comm_view = cursor_comm.fetchall()
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/myQ_detail.html", {"detail_view":detail_view, "comm_view":comm_view})

@csrf_exempt
def myq_delete(request):
    # 내 문의글 상세보기에서 삭제 버튼 클릭시 여기로
    global conn;
    cursor_myq = conn.cursor()
    cursor_comm = conn.cursor()
    qnum = request.GET["qnum"]
    # print(" 지우고 싶은 번호 : ", qnum)
    del_myq = 'delete from question where qnum = :qnum'
    del_comm = 'delete from comm where qnum = :qnum'
    cursor_myq.execute(del_myq, qnum=qnum)
    cursor_comm.execute(del_comm, qnum=qnum)
    conn.commit()
    # cursor.close()
    # conn.close()
    return render(request, 'finalProject/myQ_deleted.html')

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
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/notice_gogzy.html", {"nlist": nlist})

# 공지글 클릭해서 상세보기
def notice_detail(request):
    global conn;
    # 공지사항들 중에서 클릭한 글만 보곡 싶을때
    # 해당 공지글의 번호를 가져온다
    nnum = request.GET["nnum"]
    print("qnum : ",nnum)
    # 로그인 아이디 세션 가져오기
    member_id = request.session.get('mid')
    cursor = conn.cursor()
    noti_detail = 'select * from notice where nnum = :nnum'
    cursor.execute(noti_detail, nnum=nnum)
    conn.commit()
    noti_detail = cursor.fetchall()
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/notice_view1.html", {"noti_detail":noti_detail})

def review(request):
    global conn;  # 전역변수 사용 위해
    cursor = conn.cursor()
    cursor.execute('select*from review')
    rlist = cursor.fetchall
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/review.html", {"rlist":rlist})

def up_review(request):
    global conn;
    cursor = conn.cursor()
    mid = request.session.get("mid")
    if (mid != None):
        # cursor.close()
        # conn.commit()
        # conn.close()
        return render(request, 'finalProject/review_upload.html')
    else:
        # cursor.close()
        # conn.commit()
        # conn.close()
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
            # cursor.close()
            # conn.close()
            return render(request, "finalProject/review_upload.html")
        else:
            return render(request, 'finalProject/login_required.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def review_detail(request):
    global conn;
    cursor_review = conn.cursor()
    cursor_rehit = conn.cursor()
    # 리뷰 중에서 클릭한 글만 보곡 싶을때
    # 해당 리뷰 번호를 가져온다
    renum = request.GET["renum"]
    print("renum : ", renum)

    # cache ; 리뷰 글 번호를 cache로 등록
    # cache.set('renum', renum, None)
    # renum_compare = cache.get('renum')
    # print("방문 페이지 : ", renum_compare)

    # 조회수 증가를 위해 rehit 가져오기
    # rehit 를 가져오기 위해 .get 을 붙여준다
    rehit = request.GET.get("rehit")
    print("현재 조회수 :", rehit)
    print("rehit 타입 : ", type(rehit))
    rehit = int(rehit)
    print("rehit 타입2 : ", type(rehit))
    rehit = rehit+1
    # 로그인 아이디 세션 가져오기
    # member_id = request.session.get('mid')
    # cip = get_client_ip(request)
    # print("ip 확인 : ", cip)
    # update sawon set sahire = to_date('2019/09/10) where sabun=83;
    hitup_sql = 'update review set rehit = :rehit where renum = :renum'
    cursor_rehit.execute(hitup_sql, rehit=rehit, renum=renum)
    conn.commit()
    # 조회수 증가 완료
    
    # 상세보기 출력
    re_detail = 'select * from review where renum = :renum'
    cursor_review.execute(re_detail, renum=renum)
    detail_review = cursor_review.fetchall()
    # cursor.close()
    # conn.close()
    return render(request, 'finalProject/review_detail1.html',{"detail_review":detail_review})

def hit_up(request):
    rehit = request.GET.get("rehit") + 1
    return hit_up

# 승마장 추천
def riderecom1(request):
    global conn;  # 전역변수 사용 위해
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from place')
    plist = cursor.fetchall()
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/sungma_chu.html", {"plist": plist})

# 승마체험장 추천에서 radio 사용 하는 함수
def rideSearch(request):
    global conn;  # 전역변수 사용 위해
    request.POST.getlist('chk_pplace')
    chk_slct = request.POST.get('chk_pplace')
    print(chk_slct)
    cursor = conn.cursor()
    # clob 데이터 타입은 char 로 바꿔서 바인딩 해야 한다 https://www.warevalley.com/support/orange_view.asp?page=30&num=11943
    sql_chk = 'select * from place where to_char(pplace) =:pplace'
    # where to_char(clob_column) = :clob_column
    cursor.execute(sql_chk, pplace=chk_slct)
    # res1 = cursor.execute(sql_chk, pplace=chk_slct)
    res2 = cursor.fetchall()
    print("selelct where 쓴 결과 : ",res2) # fechall 괄호 안쓰면 object 로 넘어온다
    # cursor.close()
    # conn.close()
    return render(request, 'finalProject/sungma_radio1.html',{"res2": res2})  #, {'srch': srch, 'w': w}

def ride1(request):
    return render(request, "finalProject/sungma_sogae.html")

def race1(request):
    return render(request, "finalProject/gyungma_sogae.html")

def rideintro1(request):
    global conn;  # 전역변수 사용 위해
    cursor = conn.cursor()
    cursor.execute('select*from place')
    plist = cursor.fetchall()
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/sungma_cheso.html", {'plist':plist})

# 경마 소개
def raceintro1(request):
    return render(request, "finalProject/gyungma_jangso.html")

# 풋터
def footer(request):
    return render(request, "finalProject/footer.html")




