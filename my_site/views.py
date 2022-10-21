from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'detail.html', context)
