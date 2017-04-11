from django.conf.urls import url
from .views import EmailsView

urlpatterns = [
    url(r'^subscribe/$', EmailsView.as_view()),
]
