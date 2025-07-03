from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index (request: HttpRequest) -> HttpResponse:
    title = "Curso de Django"
    return render(request, "index.html", {
        "title": title
    })

def hello (request, word) -> HttpResponse:
    return HttpResponse(f"Hello, {word}! This is the accounts app.")

def about (request: HttpRequest) -> HttpResponse:
    about_info = {
        "title": "About Us",
        "description": "This is a sample Django application to demonstrat e basic views and templates.",
        "name_app": "Django Accounts App",
    }
    return render(request, "about.html", about_info)

def projects (request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def tasks (request: HttpRequest, id) -> HttpResponse:
    task = get_object_or_404(Task, id=id)
    return render(request, "tasks.html", {"task": task})
