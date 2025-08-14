from django.urls import path
from . import views

urlpatterns=[
    path('',views.home.as_view(),name='home'),
    path('get_news/',views.get_news.as_view(),name='get_news'),
]