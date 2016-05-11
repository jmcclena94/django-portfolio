from django.views.generic import ListView
from projects.models import Project
from forms import ProjectForm


class ProjectView(ListView):
    """View for list of projects."""

    template_name = 'portfolio/templates/projects.html'
    model = Project


class AddPhotoView(ListView):
    """View to add a new project."""
