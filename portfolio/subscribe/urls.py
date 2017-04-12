from django.conf.urls import url
from .views import EmailsView, EmailsList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^subscribe/$', EmailsView.as_view()),
    url(r'^emails/$', EmailsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
