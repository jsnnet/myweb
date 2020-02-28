from django.contrib import admin
from finalProject.models import MyPick,Horse

# Register your models here.
class FinalProjectAdmin(admin.ModelAdmin):
    list_display = ("question","ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8","ans9","ans10",
                    "ans11","ans12","ans13","ans14","ans15","ans16","ans17","ans18","ans19","ans20",
                    "ans21","ans22","ans23","ans24","ans25","ans26","ans27","ans28","ans29","ans30",
                    "ans31","ans32","ans33","ans34","ans35","ans36","ans37","ans38","ans39","ans40",
                    "ans41","ans42","ans43","ans44","ans45","ans46","ans47","ans48","ans49","ans50",
                    "ans51","ans52","ans53","ans54","ans55","ans56","ans57","ans58","ans59","ans60",
                    "ans61","ans62","ans63","ans64","ans65","ans66","ans67","ans68","ans69","ans70",
                    "ans71","ans72","ans73","ans74","ans75","ans76","ans77","ans78")

# Admin에 등록
admin.site.register(MyPick,FinalProjectAdmin)
admin.site.register(Horse)