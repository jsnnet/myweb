from django.db import models
from django.contrib.auth.models import User
# 위와 같이 하면 security 부분 맡게된다?
from django.forms import ModelForm

# Create your models here.
# Django의 내장 폼이다.
class Back(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)