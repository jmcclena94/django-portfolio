from django.db import models
from portfolio import settings


class Project(models.Model):
    """Project model."""

    class Meta:
        ordering = ['date_uploaded']

    def __str__(self):
        return self.title

    cover = models.ImageField(upload_to='covers/')
    splash = models.ImageField(upload_to='splash/', blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=255, blank=True)
    github = models.URLField(max_length=255)
