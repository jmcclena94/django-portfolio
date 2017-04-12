from django.db import models


class Emails(models.Model):
    """Emails model."""

    email = models.EmailField(max_length=255, default='')
