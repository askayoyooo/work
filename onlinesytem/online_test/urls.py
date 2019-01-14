"""onlinesytem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from online_test import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('add_project', views.add_project, name='add_projects'),
    path('edit_project/<int:nid>/', views.edit_project, name='edit_projects'),
    path('project_info/<int:nid>/', views.project_info, name='project_info'),
    path('add_project_info/<int:nid>/', views.add_project_info, name='add_project_info'),
    path('edit_project_info/<int:nid>/', views.edit_project_info, name='edit_project_info'),

]
