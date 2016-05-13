from django.conf.urls import url, include
from django.contrib import admin
from portfolio.views import HomepageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', HomepageView.as_view()),
    url(r'^home/', include('projects.urls')),
]
