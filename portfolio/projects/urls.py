from django.conf.urls import url
from .views import ProjectView, ProjectDetailView, AboutView

urlpatterns = [
    url(r'^projects/$', ProjectView.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', ProjectDetailView.as_view()),
    url(r'^about/$', AboutView.as_view()),
]
