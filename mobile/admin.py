from django.contrib import admin
from mobile.models import Profile1

# Register your models here.

class Profile1Admin(admin.ModelAdmin):
    #
    list_display = ('username','password','icon','age','gender','location','job','message','skills','experience')


admin.site.register(Profile1,Profile1Admin),