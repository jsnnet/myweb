from django.db import models

# Create your models here.
# 데이터베이스로 만들어질 때 규칙: address.Address -> address_address로 소문자로 바뀐다
class Address(models.Model): # 클래스이지 DB는 아니다
    # DB의 자료형을 따왔다
    # models를 상속 받아서 모델을 정의해야 한다

    # 컬럼명 = (속성) 데이터 타입, 속성값을 인자로 가지는 함수
    # sequence 처럼 버ㅕㄴ호를 자동으로 증가시켜주는 기능 가진 함수
    idx = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
