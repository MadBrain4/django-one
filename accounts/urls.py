from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('hello/<str:word>/', views.hello, name='hello'),
    path('index/', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('tasks/<int:project_id>/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
]
