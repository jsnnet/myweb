#member아래 forms.py
from django.forms import ModelForm
from django.contrib.auth.models import User
#회원가입 폼 만들기
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","email","password"]

#로그인 폼
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]
