from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from projects.models import Project


class ProjectView(ListView):
    """View for list of projects."""

    template_name = 'projects.html'
    model = Project


class ProjectDetailView(DetailView):
    """View for project detail."""

    template_name = 'project_detail.html'
    model = Project
