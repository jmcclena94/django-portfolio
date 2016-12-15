from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Blog


class BlogView(ListView):
    """View for list of blogs."""

    template_name = 'blogs.html'
    model = Blog


class BlogDetailView(DetailView):
    """View for project detail."""

    template_name = 'blog-detail.html'
    model = Blog
