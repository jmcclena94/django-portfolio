from django.views.generic.edit import CreateView
from subscribe.models import Emails
from subscribe.serializers import EmailsSerializer
from rest_framework import generics


class EmailsView(CreateView):
    """View for list of blogs."""

    template_name = 'subscribe.html'
    model = Emails
    fields = ['email']
    success_url = '/blog'


class EmailsList(generics.ListAPIView):
    """List all emails."""
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer
