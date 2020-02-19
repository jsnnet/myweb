#member아래 forms.py
from django.forms import ModelForm
from django.contrib.auth.models import User

#로그인 폼
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]
