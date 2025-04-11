import imp
from django.urls import path,register_converter
from . import views,converts

register_converter(converts.FloatUrlParameterConverter, 'float')

urlpatterns=[
    path('tasklist/',views.TaskListView.as_view()),
    path('taskdatails/<int:pk>',views.TaskDetail.as_view(),name='taskdetails'),
    path("createtask/",views.TaskCreation.as_view(),name='createtask'),
    path('resettasks/',views.ResetTasks.as_view(),name='resettasks'),
   path('get-city/<float:lat>/<float:lng>/', views.getcity)
]