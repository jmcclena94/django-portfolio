from django.views.generic.edit import CreateView, FormView
from subscribe.forms import UnsubscribeForm
from subscribe.models import Emails
from subscribe.serializers import EmailsSerializer
from rest_framework import generics
from django.http import HttpResponseRedirect


class SubscribeView(CreateView):
    """Subscribe view."""

    template_name = 'subscribe.html'
    model = Emails
    fields = ['email']
    success_url = '/blog'


class UnsubscribeView(FormView):
    """Unsubscribe view."""

    template_name = 'unsubscribe.html'
    form_class = UnsubscribeForm

    def form_valid(self, form):
        success_url = '/blog'
        address = form.cleaned_data['email']
        Emails.objects.filter(email=address).delete()
        return HttpResponseRedirect(success_url)


class EmailsList(generics.ListAPIView):
    """List all emails."""
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer
