from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from projects.models import Project, About


class ProjectView(ListView):
    """View for list of projects."""

    template_name = 'projects.html'
    model = Project


class ProjectDetailView(DetailView):
    """View for project detail."""

    template_name = 'project-detail.html'
    model = Project


class AboutView(ListView):
    """About me view."""

    template_name = 'about.html'
    model = About
