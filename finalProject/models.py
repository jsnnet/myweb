from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.
# 데이터베이스로 만들어질 때 규칙: address.Address -> address_address로 소문자로 바뀐다
class JoinForm(models.Model): # 클래스이지 DB는 아니다
    # DB의 자료형을 따왔다
    # models를 상속 받아서 모델을 정의해야 한다
    # 컬럼명 = (속성) 데이터 타입, 속성값을 인자로 가지는 함수
    # sequence 처럼 버ㅕㄴ호를 자동으로 증가시켜주는 기능 가진 함수
    # 회원 테이블의 관리자 (madmin) 인지 아닌지 가입시 구분
    ADMIN_CHOICES = (
        ('0','회원'),
        ('1','관리자'),
    )
    mnum = models.AutoField(primary_key = True)
    mid = models.CharField(max_length=50, blank=True, null=True, unique=True)
    mpwd = models.CharField(max_length=50, blank=True, null=False)
    mname = models.CharField(max_length=50, blank=True, null=False)
    mtel = models.IntegerField(blank=True, null=False)
    madmin = models.CharField(max_length=10, choices=ADMIN_CHOICES, null=True)
    mdate = models.DateTimeField(auto_now_add=True)

# Django의 내장 폼이다.
class UserForm(ModelForm):
    # 클래스를 안에서 정의
    # 내부 클래스 : 클래스를 생성하도록 정의하는 클래스
    class Meta:
        # Django 에서 제공해주는 사용자 정보를 모델로 사용하겠다는 의미
        model = User
        fields = ["username","email","password"] #Django 에서 제공하는 보안적용된 필드

class MyPick(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    # 설문 문제
    question=models.TextField(null=True)
    # 답변
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)
    ans5 = models.TextField(null=True)
    ans6 = models.TextField(null=True)
    ans7 = models.TextField(null=True)
    ans8 = models.TextField(null=True)
    ans9 = models.TextField(null=True)
    ans10 = models.TextField(null=True)
    ans11 = models.TextField(null=True)
    ans12 = models.TextField(null=True)
    ans13 = models.TextField(null=True)
    ans14 = models.TextField(null=True)
    ans15 = models.TextField(null=True)
    ans16 = models.TextField(null=True)
    ans17 = models.TextField(null=True)
    ans18 = models.TextField(null=True)
    ans19 = models.TextField(null=True)
    ans20 = models.TextField(null=True)
    ans21 = models.TextField(null=True)
    ans22 = models.TextField(null=True)
    ans23 = models.TextField(null=True)
    ans24 = models.TextField(null=True)
    ans25 = models.TextField(null=True)
    ans26 = models.TextField(null=True)
    ans27 = models.TextField(null=True)
    ans28 = models.TextField(null=True)
    ans29 = models.TextField(null=True)
    ans30 = models.TextField(null=True)
    ans31 = models.TextField(null=True)
    ans32 = models.TextField(null=True)
    ans33 = models.TextField(null=True)
    ans34 = models.TextField(null=True)
    ans35 = models.TextField(null=True)
    ans36 = models.TextField(null=True)
    ans37 = models.TextField(null=True)
    ans38 = models.TextField(null=True)
    ans39 = models.TextField(null=True)
    ans40 = models.TextField(null=True)
    ans41 = models.TextField(null=True)
    ans42 = models.TextField(null=True)
    ans43 = models.TextField(null=True)
    ans44 = models.TextField(null=True)
    ans45 = models.TextField(null=True)
    ans46 = models.TextField(null=True)
    ans47 = models.TextField(null=True)
    ans48 = models.TextField(null=True)
    ans49 = models.TextField(null=True)
    ans50 = models.TextField(null=True)
    ans51 = models.TextField(null=True)
    ans52 = models.TextField(null=True)
    ans53 = models.TextField(null=True)
    ans54 = models.TextField(null=True)
    ans55 = models.TextField(null=True)
    ans56 = models.TextField(null=True)
    ans57 = models.TextField(null=True)
    ans58 = models.TextField(null=True)
    ans59 = models.TextField(null=True)
    ans60 = models.TextField(null=True)
    ans61 = models.TextField(null=True)
    ans62 = models.TextField(null=True)
    ans63 = models.TextField(null=True)
    ans64 = models.TextField(null=True)
    ans65 = models.TextField(null=True)
    ans66 = models.TextField(null=True)
    ans67 = models.TextField(null=True)
    ans68 = models.TextField(null=True)
    ans69 = models.TextField(null=True)
    ans70 = models.TextField(null=True)
    ans71 = models.TextField(null=True)
    ans72 = models.TextField(null=True)
    ans73 = models.TextField(null=True)
    ans74 = models.TextField(null=True)
    ans75 = models.TextField(null=True)
    ans76 = models.TextField(null=True)
    ans77 = models.TextField(null=True)
    ans78 = models.TextField(null=True)
    # 설문진행 상태 y = 진행중, n = 종료
    status = models.CharField(max_length=1, default="y")

class Horse(models.Model):
    # 테이블 2개 조인
    answer_idx = models.AutoField(primary_key = True)
    # Survey 모델의 pk, Foreign key
    survey_idx = models.IntegerField()
    # 응답번호
    num = models.IntegerField()