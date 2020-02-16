from django.urls import path
from mobile import views
urlpatterns = [
    path("",views.home)
]