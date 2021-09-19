from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
HTML_TEMPLATE_FOLDER = 'app_projects/'

# Dict of projects to display
list_projects = [
    {'id': '1',
     'title': 'Ecommerce site',
     'description': 'Fully functional ecommerce site'
     },
    {'id': '2',
     'title': 'Portfolio site',
     'description': 'Built out portfolio website'
     },
    {'id': '3',
     'title': 'Social networking site',
     'description': 'Test social networking site'
     }
]


def get_projects(request):
    page = 'projects'
    number = 9

    return render(request,
                  template_name=HTML_TEMPLATE_FOLDER+'projects.html',
                  context={'page': page,
                           'number': number,
                           'projects': list_projects})


def get_project(request, pk):
    """
    Given a request, and a primary key (pk), returns a single project as a response.

    Note, the name 'pk' must match the urlpatterns argument name exactly - i.e. 'project/<str:pk>'
    """
    project_object = None
    for project in list_projects:
        if project['id'] == pk:
            project_object = project
    return render(request,
                  template_name=HTML_TEMPLATE_FOLDER+'single-project.html',
                  context={'project': project_object})
