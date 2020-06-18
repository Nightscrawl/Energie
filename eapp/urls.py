from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('extypes/', views.getExerciseTypes, name='extypes'),
    path('exercises/', views.getExercises, name='exercises'),
    path('exdetails/<int:id>', views.exerciseDetails, name='exdetails'),
    path('newexercise/', views.newExercise, name='newexercise'),
    path('loginmessage/', views.loginMessage, name='loginmessage'),
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
]