import imp
from django.urls import path
from . import views

urlpatterns=[
    path('<str:catigory>/',views.home,name='home'),
]