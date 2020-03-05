# 분석을 위한 import #################################################################
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc
# import missingno as msno
import csv
# import tensorflow as tf
# from PIL import Image
import os, glob, numpy as np

# keras 모델을 읽어오기 위한 keras 모델
# from pandas import read_csv
# from tensorflow.python.keras.models import load_model
# from keras.models import model_from_json
# import scipy.stats as stats
# import matplotlib.pyplot as plt
# 분석을 위한 import #################################################################

from django.shortcuts import render, redirect
import cx_Oracle as oci
from django.views.decorators.csrf import csrf_exempt
from .models import JoinForm
# ==============================================================================지도 api (google) 와 folium 패키지 사용
# folium 설치가 안되어 있다면 pip install 해줘야 사용가능
import folium
# import googlemaps
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
from finalProject.models import Select,Horse
#############################################


# 단축키 참고
# https://kgu0724.tistory.com/95

# DB 사용에 따른 conn 연결 (전역변수 사용하려면 변수 앞에 global 써주고 함수마다 변수 선언해야만 한다)
# conn = oci.connect('doosun/doosun@localhost:1521/xe')
conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
# conn = oci.connect('doosun/doosun@192.168.0.7:1521/xe')
# conn = oci.connect('final_teamB_xman/test11@localhost:1521/xe')
# conn = oci.connect("finalB_horse/test11@192.168.0.149:1521/xe", encoding="UTF-8")

########################################### 작성해야 할 아래에 있던 코드 위로 올려 놓음 ############################################################################

# 이미지 띄우기
def info_run_horse(request):
    return render(request, "finalProject/info_run_horse.html")

def info_ride_horse(request):
    return render(request, "finalProject/info_ride_horse.html")

# 경마 누가 주인공이냐
def whoiszoo1(request):
    # 커넥션을 반환하는 함수
    # global conn
    def connections():
        # global conn
        try:
            conn = oci.connect("finalB_horse/test11@192.168.0.149:1521/xe", encoding="UTF-8")
        except oci.DatabaseError as e:
            conn = "접속 예외 발생"
            print(e)
            return
        return conn

    def select_predict(gnum):
        conn = connections()
        cursor = conn.cursor()
        sql_select = "select p.pnum, h.hname, h.hage, h.hsex, h.hsanji, \
            h.hweight, h.htotal, h.hwin, h.hpicture, p.ptime from horse h, predict p \
            where h.hnum = p.hnum and p.gnum = :gnum order by 1 asc"
        cursor.execute(sql_select, {"gnum": gnum})
        numRows = 3
        res_select_predict = cursor.fetchmany(numRows=numRows)
        gmeter = res_select_predict[0][0]
        cursor.close()
        conn.close()

        return res_select_predict

    # 해당 경기의 우승마 데이터 반환
    def select_winner(gnum):
        conn = connections()
        cursor = conn.cursor()
        sql_select = "select w.wnum, h.hname, h.hage, h.hsex, h.hsanji, \
            h.hweight, h.htotal, h.hwin, h.hpicture from horse h, winner w \
            where h.hnum = w.hnum and w.gnum = :gnum order by 1 asc"
        cursor.execute(sql_select, {"gnum": gnum})
        numRows = 3
        res_select_winner = cursor.fetchmany(numRows=numRows)
        gmeter = res_select_winner[0][0]
        cursor.close()
        conn.close()

        return res_select_winner

    # 메인 메서드
    def predict_list1(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 1;
        predict = select_predict(gnum)
        # predict_info(gnum)
        return predict

    def predict_list2(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 2;
        predict = select_predict(gnum)
        return predict

    def predict_list3(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 3;
        predict = select_predict(gnum)
        return predict

    def predict_list4(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 4;
        predict = select_predict(gnum)
        return predict

    def predict_list5(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 5;
        predict = select_predict(gnum)
        return predict

    def predict_list6(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 6;
        predict = select_predict(gnum)
        return predict

    def predict_list7(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 7;
        predict = select_predict(gnum)
        return predict

    def predict_list8(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 8;
        predict = select_predict(gnum)
        return predict

    print("여기까진?")
    # 아래는 라운드 별 숫자값 넣어주는 곳
    # 출력해보기
    print("최종결과 : ", predict_list1(1))
    print("최종결과 : ", predict_list2(2))
    print("최종결과 : ", predict_list3(3))
    print("최종결과 : ", predict_list4(4))
    print("최종결과 : ", predict_list5(5))
    print("최종결과 : ", predict_list6(6))
    print("최종결과 : ", predict_list7(7))
    print("최종결과 : ", predict_list8(8))

    # html에 리스트 값으로 넘겨주기 준비
    predict_list1 = predict_list1(1)
    predict_list2 = predict_list2(2)
    predict_list3 = predict_list3(3)
    predict_list4 = predict_list4(4)
    predict_list5 = predict_list5(5)
    predict_list6 = predict_list6(6)
    predict_list7 = predict_list7(7)
    predict_list8 = predict_list8(8)
    return render(request, "finalProject/whois_juingong.html", {"predict_list1":predict_list1,"predict_list2":predict_list2,
                                                                "predict_list3":predict_list3,"predict_list4":predict_list4,
                                                                "predict_list5":predict_list5,"predict_list6":predict_list6,
                                                                "predict_list7":predict_list7,"predict_list8":predict_list8})

# 오늘의 주인공은?
def todayzoo1(request):
    # 커넥션을 반환하는 함수
    # global conn
    def connections():
        # global conn
        try:
            conn = oci.connect("finalB_horse/test11@192.168.0.149:1521/xe", encoding="UTF-8")
        except oci.DatabaseError as e:
            conn = "접속 예외 발생"
            print(e)
            return
        return conn

    def select_predict(gnum):
        conn = connections()
        cursor = conn.cursor()
        sql_select = "select p.pnum, h.hname, h.hage, h.hsex, h.hsanji, \
            h.hweight, h.htotal, h.hwin, h.hpicture, p.ptime from horse h, predict p \
            where h.hnum = p.hnum and p.gnum = :gnum order by 1 asc"
        cursor.execute(sql_select, {"gnum": gnum})
        numRows = 3
        res_select_predict = cursor.fetchmany(numRows=numRows)
        gmeter = res_select_predict[0][0]
        cursor.close()
        conn.close()

        return res_select_predict

    # 해당 경기의 우승마 데이터 반환
    def select_winner(gnum):
        conn = connections()
        cursor = conn.cursor()
        sql_select = "select w.wnum, h.hname, h.hage, h.hsex, h.hsanji, \
            h.hweight, h.htotal, h.hwin, h.hpicture from horse h, winner w \
            where h.hnum = w.hnum and w.gnum = :gnum order by 1 asc"
        cursor.execute(sql_select, {"gnum": gnum})
        numRows = 3
        res_select_winner = cursor.fetchmany(numRows=numRows)
        gmeter = res_select_winner[0][0]
        cursor.close()
        conn.close()

        return res_select_winner

    # 메인 메서드
    def winner_list1(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 1;
        winner = select_winner(gnum)
        # winner_info(gnum)
        return winner

    def winner_list2(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 2;
        winner = select_winner(gnum)
        return winner

    def winner_list3(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 3;
        winner = select_winner(gnum)
        return winner

    def winner_list4(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 4;
        winner = select_winner(gnum)
        return winner

    def winner_list5(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 5;
        winner = select_winner(gnum)
        return winner

    def winner_list6(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 6;
        winner = select_winner(gnum)
        return winner

    def winner_list7(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 7;
        winner = select_winner(gnum)
        return winner

    def winner_list8(gnum):
        # 예측 데이터 반환 메서드 실행
        # 1을 강제로 넣었는데 실제로는
        # html 에서 숫자를 받아서 메인메서드에서 받아서
        # 실행해야 하는 부분입니다.
        gnum = 8;
        winner = select_winner(gnum)
        return winner

    print("여기까진?")
    # 아래는 라운드 별 숫자값 넣어주는 곳
    # 출력해보기
    print("최종결과 : ", winner_list1(1))
    print("최종결과 : ", winner_list2(2))
    print("최종결과 : ", winner_list3(3))
    print("최종결과 : ", winner_list4(4))
    print("최종결과 : ", winner_list5(5))
    print("최종결과 : ", winner_list6(6))
    print("최종결과 : ", winner_list7(7))
    print("최종결과 : ", winner_list8(8))

    # html에 리스트 값으로 넘겨주기 준비
    winner_list1 = winner_list1(1)
    winner_list2 = winner_list2(2)
    winner_list3 = winner_list3(3)
    winner_list4 = winner_list4(4)
    winner_list5 = winner_list5(5)
    winner_list6 = winner_list6(6)
    winner_list7 = winner_list7(7)
    winner_list8 = winner_list8(8)
    return render(request, "finalProject/today_juingong.html",
                  {"winner_list1": winner_list1, "winner_list2": winner_list2,
                   "winner_list3": winner_list3, "winner_list4": winner_list4,
                   "winner_list5": winner_list5, "winner_list6": winner_list6,
                   "winner_list7": winner_list7, "winner_list8": winner_list8})

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
    survey = Select.objects.filter(status='y').order_by("-survey_idx")[0]
    return render(request, "finalProject/whois_onepick1.html", {"survey":survey})

@csrf_exempt
def save_survey(request):
    # survey_idx=request.POST["survey_idx"]
    # print(survey_idx)
    # print("넘어오는 num 값 : ", request.POST["num"])
    survey_dto = Horse(survey_idx=request.POST["survey_idx"],num=request.POST["num"])
    # print("ans:",request.POST["ans"])
    ans = request.POST["ans"]
    # print("투표 결과 : ", ans)
    survey_dto.save()
    return render(request,"finalProject/success.html",{"ans":ans})

def show_result(request):
    idx = request.GET['survey_idx']
    ans = Select.objects.get(survey_idx=idx)
    print("ans : ",ans)
    answer_dto = [ans.ans1,ans.ans2,ans.ans3,ans.ans4,ans.ans5,ans.ans6,ans.ans7,ans.ans8,ans.ans9,ans.ans10,
                  ans.ans11,ans.ans12,ans.ans13,ans.ans14,ans.ans15,ans.ans16,ans.ans17,ans.ans18,ans.ans19,ans.ans20,
                  ans.ans21,ans.ans22,ans.ans23,ans.ans24,ans.ans25,ans.ans26,ans.ans27,ans.ans28,ans.ans29,ans.ans30,
                  ans.ans31,ans.ans32,ans.ans33,ans.ans34,ans.ans35,ans.ans36,ans.ans37,ans.ans38,ans.ans39,ans.ans40,
                  ans.ans41,ans.ans42,ans.ans43,ans.ans44,ans.ans45,ans.ans46,ans.ans47,ans.ans48,ans.ans49,ans.ans50,
                  ans.ans51,ans.ans52,ans.ans53,ans.ans54,ans.ans55,ans.ans56,ans.ans57,ans.ans58,ans.ans59,ans.ans60,
                  ans.ans61,ans.ans62,ans.ans63,ans.ans64,ans.ans65,ans.ans66,ans.ans67,ans.ans68,ans.ans69,ans.ans70,
                  ans.ans71,ans.ans72,ans.ans73,ans.ans74,ans.ans75,ans.ans76,ans.ans77,ans.ans78]

    surveyList = Select.objects.raw("""
    select 
    survey_idx,num,count(*) sum_num,
    round((select count(*) from finalProject_horse
    where survey_idx=a.survey_idx and num=a.num) * 100.0
    /(select count(*) from finalProject_horse 
    where survey_idx=a.survey_idx)
    ,1) rate
    from finalProject_horse a where survey_idx=%s
    group by survey_idx,num
    order by num
    """, idx)
    surveyList = zip(surveyList, answer_dto)
    # print("surveyList : ", surveyList)
    # print("answer_dto : ", answer_dto)
    # count = Horse.objects.all().count()
    return render(request, "finalProject/whois_onepick_result6.html", {"surveyList":surveyList})

def todayzoo1_app(request):
    def whoiszoo1(request):
        # 커넥션을 반환하는 함수
        # global conn
        def connections():
            # global conn
            try:
                conn = oci.connect("finalB_horse/test11@192.168.0.149:1521/xe", encoding="UTF-8")
            except oci.DatabaseError as e:
                conn = "접속 예외 발생"
                print(e)
                return
            return conn

        def select_predict(gnum):
            conn = connections()
            cursor = conn.cursor()
            sql_select = "select p.pnum, h.hname, h.hage, h.hsex, h.hsanji, \
                h.hweight, h.htotal, h.hwin, h.hpicture, p.ptime from horse h, predict p \
                where h.hnum = p.hnum and p.gnum = :gnum order by 1 asc"
            cursor.execute(sql_select, {"gnum": gnum})
            numRows = 3
            res_select_predict = cursor.fetchmany(numRows=numRows)
            gmeter = res_select_predict[0][0]
            cursor.close()
            conn.close()

            return res_select_predict

        # 해당 경기의 우승마 데이터 반환
        def select_winner(gnum):
            conn = connections()
            cursor = conn.cursor()
            sql_select = "select w.wnum, h.hname, h.hage, h.hsex, h.hsanji, \
                h.hweight, h.htotal, h.hwin, h.hpicture from horse h, winner w \
                where h.hnum = w.hnum and w.gnum = :gnum order by 1 asc"
            cursor.execute(sql_select, {"gnum": gnum})
            numRows = 3
            res_select_winner = cursor.fetchmany(numRows=numRows)
            gmeter = res_select_winner[0][0]
            cursor.close()
            conn.close()

            return res_select_winner

        # 메인 메서드
        def predict_list1(gnum):
            # 예측 데이터 반환 메서드 실행
            # 1을 강제로 넣었는데 실제로는
            # html 에서 숫자를 받아서 메인메서드에서 받아서
            # 실행해야 하는 부분입니다.
            gnum = 1;
            predict = select_predict(gnum)
            # predict_info(gnum)
            return predict

        def predict_list2(gnum):
            # 예측 데이터 반환 메서드 실행
            # 1을 강제로 넣었는데 실제로는
            # html 에서 숫자를 받아서 메인메서드에서 받아서
            # 실행해야 하는 부분입니다.
            gnum = 2;
            predict = select_predict(gnum)
            return predict

        def predict_list3(gnum):
            # 예측 데이터 반환 메서드 실행
            # 1을 강제로 넣었는데 실제로는
            # html 에서 숫자를 받아서 메인메서드에서 받아서
            # 실행해야 하는 부분입니다.
            gnum = 3;
            predict = select_predict(gnum)
            return predict

        def predict_list4(gnum):
            # 예측 데이터 반환 메서드 실행
            # 1을 강제로 넣었는데 실제로는
            # html 에서 숫자를 받아서 메인메서드에서 받아서
            # 실행해야 하는 부분입니다.
            gnum = 4;
            predict = select_predict(gnum)
            return predict

        def predict_list5(gnum):
            # 예측 데이터 반환 메서드 실행
            # 1을 강제로 넣었는데 실제로는
            # html 에서 숫자를 받아서 메인메서드에서 받아서
            # 실행해야 하는 부분입니다.
            gnum = 5;
            predict = select_predict(gnum)
            return predict

        def predict_list6(gnum):
            # 예측 데이터 반환 메서드 실행
            # 1을 강제로 넣었는데 실제로는
            # html 에서 숫자를 받아서 메인메서드에서 받아서
            # 실행해야 하는 부분입니다.
            gnum = 6;
            predict = select_predict(gnum)
            return predict

        def predict_list7(gnum):
            # 예측 데이터 반환 메서드 실행
            # 1을 강제로 넣었는데 실제로는
            # html 에서 숫자를 받아서 메인메서드에서 받아서
            # 실행해야 하는 부분입니다.
            gnum = 7;
            predict = select_predict(gnum)
            return predict

        def predict_list8(gnum):
            # 예측 데이터 반환 메서드 실행
            # 1을 강제로 넣었는데 실제로는
            # html 에서 숫자를 받아서 메인메서드에서 받아서
            # 실행해야 하는 부분입니다.
            gnum = 8;
            predict = select_predict(gnum)
            return predict

        print("여기까진?")
        # 아래는 라운드 별 숫자값 넣어주는 곳
        # 출력해보기
        print("최종결과 : ", predict_list1(1))
        print("최종결과 : ", predict_list2(2))
        print("최종결과 : ", predict_list3(3))
        print("최종결과 : ", predict_list4(4))
        print("최종결과 : ", predict_list5(5))
        print("최종결과 : ", predict_list6(6))
        print("최종결과 : ", predict_list7(7))
        print("최종결과 : ", predict_list8(8))

        # html에 리스트 값으로 넘겨주기 준비
        predict_list1 = predict_list1(1)
        predict_list2 = predict_list2(2)
        predict_list3 = predict_list3(3)
        predict_list4 = predict_list4(4)
        predict_list5 = predict_list5(5)
        predict_list6 = predict_list6(6)
        predict_list7 = predict_list7(7)
        predict_list8 = predict_list8(8)
        return render(request, "finalProject/whois_juingong.html",
                      {"predict_list1": predict_list1, "predict_list2": predict_list2,
                       "predict_list3": predict_list3, "predict_list4": predict_list4,
                       "predict_list5": predict_list5, "predict_list6": predict_list6,
                       "predict_list7": predict_list7, "predict_list8": predict_list8})
    return render(request, "finalProject/today_juingong_app.html")

##################################### 위로는 경마에 해당하는 함수들


##################################### 아래는 홈부터 작성 차례로 자리한 함수들

def home(request):
    return render(request, "finalProject/home_main.html")

def home_app(request):
    return render(request, "finalProject/home_app.html")

def join(request):
    return render(request, "finalProject/join_gaip3.html")

####################################################################### (상) sqlite 과 oracle DB에 동시 회원가입하는 부분
from django.contrib import auth
@csrf_exempt
def join_Oraclite(request):
    # global conn;
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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

    if (mid == ''):
        return render(request, 'finalProject/none_value.html')
    elif (mpwd == ''):
        return render(request, 'finalProject/none_value.html')
    elif (mname == ''):
        return render(request, 'finalProject/none_value.html')
    # elif (mtel is not ):
    #     return render(request, 'finalProject/none_value.html')
    else:
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
        # global conn;
        conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
            print("if 진입한 chk_pwd : ", chk_pwd)
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
    # global conn; #전역변수 사용 위해
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
    # global conn;  # 전역변수 사용 위해
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
    # global conn;
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
    # global conn;
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
    # global conn;  # 전역변수 사용 위해
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select * from notice order by nnum desc')
    # cursor.execute('select nnum, ntitle, ncontent, nhit, to_char(ndate) from notice')
    # print("공지 제목 날짜 : ",res)
    nlist = cursor.fetchall()
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/notice_gogzy.html", {"nlist": nlist})

# 공지글 클릭해서 상세보기
def notice_detail(request):
    # global conn;
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
    # global conn;  # 전역변수 사용 위해
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    cursor = conn.cursor()
    cursor.execute('select * from review order by 1 desc')
    rlist = cursor.fetchall
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/review.html", {"rlist":rlist})

def up_review(request):
    # global conn;
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
    # global conn; #전역변수 사용 위해
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
    # global conn;
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
    print("여기까지")
    # global conn;  # 전역변수 사용 위해
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from place')
    plist = cursor.fetchall()
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/sungma_chu.html", {"plist": plist})

# 승마장 추천
def riderecom1_app(request):
    print("여기까지")
    # global conn;  # 전역변수 사용 위해
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    cursor.execute('select*from place')
    plist = cursor.fetchall()
    # cursor.close()
    # conn.close()
    return render(request, "finalProject/sungma_chu_app.html", {"plist": plist})


# 승마체험장 추천에서 radio 사용 하는 함수
def rideSearch(request):
    # global conn;  # 전역변수 사용 위해
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
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
    # global conn;  # 전역변수 사용 위해
    conn = oci.connect('final_teamB_xman/test11@192.168.0.15:1521/xe')
    print(conn.version)
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

# def dashboard(request):
#     idx = request.GET['survey_idx']
#     # select * from  where survey_idx=1
#     ans = MyPick.objects.get(survey_idx=idx)
#     answer_dto = [ans.ans1, ans.ans2, ans.ans3, ans.ans4, ans.ans5, ans.ans6, ans.ans7, ans.ans8, ans.ans9, ans.ans10,
#                   ans.ans11, ans.ans12, ans.ans13, ans.ans14, ans.ans15, ans.ans16, ans.ans17, ans.ans18, ans.ans19,
#                   ans.ans20,
#                   ans.ans21, ans.ans22, ans.ans23, ans.ans24, ans.ans25, ans.ans26, ans.ans27, ans.ans28, ans.ans29,
#                   ans.ans30,
#                   ans.ans31, ans.ans32, ans.ans33, ans.ans34, ans.ans35, ans.ans36, ans.ans37, ans.ans38, ans.ans39,
#                   ans.ans40,
#                   ans.ans41, ans.ans42, ans.ans43, ans.ans44, ans.ans45, ans.ans46, ans.ans47, ans.ans48, ans.ans49,
#                   ans.ans50,
#                   ans.ans51, ans.ans52, ans.ans53, ans.ans54, ans.ans55, ans.ans56, ans.ans57, ans.ans58, ans.ans59,
#                   ans.ans60,
#                   ans.ans61, ans.ans62, ans.ans63, ans.ans64, ans.ans65, ans.ans66, ans.ans67, ans.ans68, ans.ans69,
#                   ans.ans70, ans.ans71, ans.ans72, ans.ans73, ans.ans74, ans.ans75, ans.ans76, ans.ans77, ans.ans78]
#
#     surveyList = MyPick.objects.raw("""
#         select survey_idx,num,count(*) sum_sum,
#         round((select count(*) from finalProject_horse
#         where survey_idx=a.survey_idx and num= a.num) * 100.0
#         /(select count(*) from finalProject_horse where survey_idx=a.survey_idx)
#         ,1) rate
#         from finalProject_horse a where survey_idx=%s
#         group by survey_idx,num
#         order by num asc
#         """, idx)
#     print("surveyList : ", surveyList)
#     surveyList = zip(surveyList, answer_dto)
#     print("surveyList 타입 : ", type(surveyList))
#     return render(request, "finalProject/dashboard.html", {"surveyList":surveyList})


