from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
HTML_TEMPLATE_FOLDER = 'app_projects/'


def get_projects(request):
    projects = Project.objects.all()
    return render(request,
                  template_name=HTML_TEMPLATE_FOLDER+'projects.html',
                  context={'projects': projects})


def get_project(request, pk):
    """
    Given a request, and a primary key (pk), returns a single project as a response.

    Note, the name 'pk' must match the urlpatterns argument name exactly - i.e. 'project/<str:pk>'
    """
    project_object = Project.objects.get(id=pk)
    return render(request,
                  template_name=HTML_TEMPLATE_FOLDER+'single-project.html',
                  context={'project': project_object})
