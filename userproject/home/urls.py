from django.conf.urls import url
from django.contrib import admin
from . import  views

urlpatterns = [
    url('login', views.loginUser, name="login"),
    url('logout', views.logoutUser, name="logout"),
    url('', views.index, name="index")
]
