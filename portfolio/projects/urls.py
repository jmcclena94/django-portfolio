from django.conf.urls import url
from .views import ProjectView, AddProjectView
from .views import UpdateProjectView, DeleteProjectView

urlpatterns = [
    url(r'^projects/$', ProjectView.as_view()),
    url(r'^projects/add/$', AddProjectView.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', UpdateProjectView.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/delete/$', DeleteProjectView.as_view()),
]
