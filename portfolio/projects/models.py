from django.db import models


class Project(models.Model):
    """Project model."""

    def __str__(self):
        return self.title

    cover = models.ImageField(upload_to='covers/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_completed = models.DateField()
    url = models.URLField(max_length=255)
    github = models.URLField(max_length=255)
