from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	#path for about page which will be the first to load
    path('', views.mainPage, name='about')
]