from django.db import models


class BlogImage(models.Model):
    """Blog image."""

class Blog(models.Model):
    """Blog model."""

    class Meta:
        ordering = ['date_uploaded']

    cover = models.ImageField(upload_to='blog/covers/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
