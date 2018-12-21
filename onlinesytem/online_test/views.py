from django.shortcuts import render, redirect
from django.contrib import auth
from online_test.forms import ProjectForm
from online_test import models


def index(request):

    return render(request, 'online_test/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=pwd)
        if user:
            return redirect("")


def projects(request):
    result = models.Project.objects.all()
    print(type(result))
    if request.method == "GET":
        return render(request, 'online_test/projects.html', {'projects': result})


def add_project(request):
    if request.method == "GET":
        obj = ProjectForm()
        print(obj)
        return render(request, 'online_test/add_project.html', {'obj': obj})
    else:
        obj = ProjectForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            models.Project.objects.create(**obj.cleaned_data)
            return redirect('projects')
        return render(request, 'online_test/add_project.html', {'obj': obj})



