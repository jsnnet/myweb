from django.db import models
from django.contrib.auth.models import User
# 위와 같이 하면 security 부분 맡게된다?
from django.forms import ModelForm

# Create your models here.
# Django의 내장 폼이다.
class UserForm(ModelForm):
    # 클래스를 안에서 정의
    # 내부 클래스 : 클래스를 생성하도록 정의하는 클래스
    class Meta:
        # Django 에서 제공해주는 사용자 정보를 모델로 사용하겠다는 의미
        model = User
        fields = ["username","email","password"] #Django 에서 제공하는 보안적용된 필드
