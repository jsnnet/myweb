from django.db import models

# Create your models here.
class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    # 설문 문제
    question=models.TextField(null=True)
    # 답변
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)
    # 설문진행 상태 y = 진행중, n = 종료
    status = models.CharField(max_length=1, default="y")

class Answer(models.Model):
    # 테이블 2개 조인
    answer_idx = models.AutoField(primary_key = True)
    # Survey 모델의 pk, Foreign key
    survey_idx = models.IntegerField()
    # 응답번호
    num = models.IntegerField()