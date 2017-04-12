from django.conf.urls import url
from .views import SubscribeView, UnsubscribeView, EmailsList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^subscribe/$', SubscribeView.as_view()),
    url(r'^unsubscribe/$', UnsubscribeView.as_view()),
    url(r'^emails/$', EmailsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
