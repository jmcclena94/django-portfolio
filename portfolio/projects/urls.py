from django.conf.urls import url
from views import ProjectView

urlpatterns = [
    url(r'^projects/$', ProjectView()),
]
