from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^amadon', include('apps.amadon.urls')),
    url(r'^courses', include('apps.courses.urls')),
    url(r'^admin/', admin.site.urls)
]
