from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('hello/<str:word>/', views.hello, name='hello'),
    path('index/', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('tasks/<int:id>/', views.tasks, name='tasks'),
]
