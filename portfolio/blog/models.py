from django.db import models


# class BlogImage(models.Model):
#     """Blog image."""
#
#     image = models.ImageField(upload_to='blog/images/%Y-%m-%d')
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#
#
# class BlogVideo(models.Model):
#     """Blog video."""
#
#     url = models.URLField(max_length=255)
#     description = models.TextField()


class Blog(models.Model):
    """Blog model."""

    class Meta:
        ordering = ['date_uploaded']

    cover = models.ImageField(upload_to='blog/covers/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
    # images = models.ManyToManyField(BlogImage)
    # videos = models.ManyToManyField(BlogVideo)
