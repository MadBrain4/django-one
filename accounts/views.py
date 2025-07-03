from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index (request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

def hello (request, word) -> HttpResponse:
    return HttpResponse(f"Hello, {word}! This is the accounts app.")

def about (request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")

def projects (request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()
    return JsonResponse(
        {
            "projects": list(projects.values("id", "name", "description"))
        },
        status=200
    )

def tasks (request: HttpRequest, id) -> HttpResponse:
    task = get_object_or_404(Task, id=id)
    return JsonResponse(
        {
            "id": task.id,
            "name": task.name,
        },
        status=200
    )
