from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mobile.models import Profile1

# Create your views here.

def home(request):
    profile = Profile1.objects.get(username="bigdata")
    print(profile)
    skillsv = []
    for e in profile.skills.split("/"):
        print(e)
        skillsv.append(e)
    experiencev = []
    for e in profile.experience.split("/"):
        print(e.strip())
        experiencev.append(e.strip())
    print(experiencev)
    reslist = zip(skillsv,experiencev)
    return render(request, "mobile/index.html",{"profile":profile,"reslist":reslist})