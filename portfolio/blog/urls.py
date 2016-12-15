from django.conf.urls import url
from .views import BlogView, BlogDetailView

urlpatterns = [
    url(r'^blog/$', BlogView.as_view()),
    url(r'^blog/(?P<pk>[0-9]+)/$', BlogDetailView.as_view()),
]
