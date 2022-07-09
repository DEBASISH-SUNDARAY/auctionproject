from django import views
from django.contrib import admin
from django.urls import path 
from Auction import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home1', views.home1, name='home1'),
    path('login', views.userlogin, name='userlogin'),
    path('signup', views.signup, name='signup'),
    path('myproduct', views.myproduct, name='myproduct'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('more', views.more, name='more'),
]