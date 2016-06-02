from django.test import TestCase
from projects.models import Project
import factory


class ProjectFactory(factory.django.DjangoModelFactory):
    """Set up Project Factory."""
    class Meta:
        model = Project
    cover = factory.django.ImageField(filename='/tmp/cover.jpg')
    splash = factory.django.ImageField(filename='/tmp/splash.jpg')
    title = 'title'
    description = 'description'
    date_uploaded = '2016-05-01'
    url = 'www.example.com'
    github = 'www.github.com'


class ProjectTest(TestCase):
    """Test project model."""

    def setUp(self):
        self.project = ProjectFactory.create()

    def test_project_title(self):
        """Test project title field."""
        self.project.title = 'title'
