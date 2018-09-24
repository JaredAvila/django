from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^post', include('apps.post.urls')),
    url(r'^ajax_demo', include('apps.ajax_demo.urls')),
    url(r'^admin/', admin.site.urls)
]
