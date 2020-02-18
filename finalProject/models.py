from django.db import models

# Create your models here.

class SignupForm(models.Model):
      mid = models.CharField(max_length=50, blank=True)
      mpwd = models.CharField(max_length=50, blank=True)
      mname = models.DateField(null=True, blank=True)
      mtel = models.CharField(max_length=50, blank=True)
      madmin = models.IntegerField(max_length=1)
      mdate = models.DateField(null=True, blank=True)