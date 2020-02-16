from django.db import models

# Create your models here.
class Board(models.Model):
    no_idx = models.AutoField(primary_key=True)
    pwd = models.TextField(null=True)
    writer = models.TextField(null=True)
    subject = models.TextField(null=True)
    content = models.TextField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)

class BBS_comm(models.Model):
    number_idx = models.AutoField(primary_key = True)
    tcode = models.IntegerField(null=False)
    comm = models.TextField(null=True)
    writer = models.TextField(null=True)
    pwd = models.TextField(null=True)
    no_idx= models.IntegerField()
