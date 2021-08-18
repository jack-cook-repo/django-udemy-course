from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_projects(request):
    return render(request, template_name='projects.html')


def get_project(request, pk):
    """
    Given a request, and a primary key (pk), returns a single project as a response.

    Note, the name 'pk' must match the urlpatterns argument name exactly - i.e. 'project/<str:pk>'
    """
    return render(request, template_name='single-project.html')