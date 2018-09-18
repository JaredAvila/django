from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('apps.users.urls')),
    url(r'^dojo/', include('apps.dojo_ninjas.urls')),
    url(r'^authors/', include('apps.book_authors.urls')),
    url(r'^admin/', admin.site.urls)
]
