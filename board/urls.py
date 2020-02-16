from board import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('upload', views.upload),
    path('add',views.add),
    path('view',views.view),

]

