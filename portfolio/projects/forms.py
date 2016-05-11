from django.forms import ModelForm
from models import Project


class ProjectForm(ModelForm):
    """Form field for projects."""

    class Meta:
        model = Project
        fields = [
            'cover',
            'title',
            'description',
            'url',
            'github',
            'date_completed'
        ]
