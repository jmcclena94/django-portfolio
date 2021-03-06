from django.conf.urls import url, include
from django.contrib import admin
from portfolio.views import HomepageView
from portfolio import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomepageView.as_view()),
    url(r'^', include('projects.urls')),
    url(r'^', include('blog.urls')),
    url(r'^', include('subscribe.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
