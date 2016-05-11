from django.views.generic import ListView
from projects.models import Project
from .forms import ProjectForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProjectView(ListView):
    """View for list of projects."""

    template_name = 'portfolio/templates/projects.html'
    model = Project


class AddProjectView(CreateView):
    """View to add a new project."""

    template_name = 'portfolio/templates/projects.html'
    model = Project


class UpdateProjectView(UpdateView):
    """View to update a new project."""

    template_name = 'portfolio/templates/projects.html'
    model = Project


class DeleteProjectView(DeleteView):
    """View to delete a new project."""

    template_name = 'portfolio/templates/projects.html'
    model = Project
