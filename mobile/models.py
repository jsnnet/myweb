from django.db import models
#from mobile.models import Profile1

# Create your models here.
class Profile1(models.Model):
    idx = models.AutoField(primary_key = True)
    username = models.CharField(max_length=10,blank=True,null=True)
    password = models.CharField(max_length=10,blank=True,null=True)
    icon = models.CharField(max_length=50,blank=True,null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    location = models.CharField(max_length=50,blank=True,null=True)
    job = models.CharField(max_length=50,blank=True,null=True)
    message = models.TextField(null=True)
    skills = models.CharField(max_length=50,blank=True,null=True)
    experience = models.TextField(null=True)
    regdate = models.DateField(auto_now=True)