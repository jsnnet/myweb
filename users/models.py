from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=50, blank=True, null=True, primary_key=True),
    password = models.CharField(max_length=50, blank=True, null=True),
