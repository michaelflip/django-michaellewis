from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', 'article.views.hello'),
    url(r'^admin/', include(admin.site.urls)),
]
