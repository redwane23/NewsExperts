from cgi import test
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path("",views.ProfileView,name='profile'),
    path('alter/',views.AlterInforamtino,name='alter'),
    path('register/',views.registerview.as_view(),name='register'),
    path('login/',views.loginview.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
]