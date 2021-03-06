from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_projects, name='projects'),
    path('project/<str:pk>', views.get_project, name='project')
]