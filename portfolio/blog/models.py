from django.db import models


class Blog(models.Model):
    """Blog model."""

    class Meta:
        ordering = ['-date_uploaded']

    cover = models.ImageField(upload_to='blog/covers/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
