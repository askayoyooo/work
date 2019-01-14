from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from online_test.forms import ProjectForm, ProjectInfoForm
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
    # print(type(result))
    if request.method == "GET":
        return render(request, 'online_test/projects.html', {'projects': result})


def add_project(request):
    if request.method == "GET":
        obj = ProjectForm()
        # print(obj)
        return render(request, 'online_test/add_project.html', {'obj': obj})
    else:
        obj = ProjectForm(request.POST)
        if obj.is_valid():
            # print(obj.cleaned_data)
            models.Project.objects.create(**obj.cleaned_data)
            return redirect('projects')
        return render(request, 'online_test/add_project.html', {'obj': obj})


def edit_project(request, nid):
    if request.method == "GET":
        ret = models.Project.objects.filter(id=nid).values().first()
        obj = ProjectForm(ret)
        return render(request, 'online_test/edit_project.html', {'nid': nid, 'obj': obj})
    else:
        obj = ProjectForm(request.POST)
        if obj.is_valid():
            # print(obj.cleaned_data)
            models.Project.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('projects')
        return render(request, 'online_test/edit_project.html', {'nid': nid, 'obj': obj})


def project_info(request, nid):
    if request.method == "GET":
        ret = models.ProjectInfo.objects.filter(id=nid).values().first()
        obj_info = ProjectInfoForm(ret)
        return render(request, 'online_test/project_info.html', {'nid': nid, 'obj_info': obj_info})
        # return HttpResponse('aaa')


def add_project_info(request, nid):
    pass


def edit_project_info(request, nid):
    if request.method == "GET":
        ret = models.ProjectInfo.objects.filter(id = nid).values().first()
        obj_info = ProjectInfoForm(ret)
        return render(request, 'online_test/edit_project_info.html', {'nid': nid, 'obj_info': obj_info})
    else:
        obj_info = ProjectInfoForm(request.POST)
        if obj_info.is_valid():
            models.ProjectInfo.objects.filter(id=nid).update(**obj_info.cleaned_data)
        return render(request, 'online_test/edit_project_info.html', {'nid': nid, 'obj_info': obj_info})


