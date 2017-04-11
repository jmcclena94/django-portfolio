from django.views.generic.list import ListView
from subscribe.models import Emails


class EmailsView(ListView):
    """View for list of blogs."""

    template_name = 'blogs.html'
    model = Emails
