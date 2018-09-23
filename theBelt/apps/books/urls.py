from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/show/(?P<id>\d+)', views.show),
    url(r'^/book/(?P<id>\d+)$', views.book),
    url(r'^/book/(?P<id>\d+)/delete', views.delete),
    url(r'^/validate$', views.validateBookReview),
    url(r'^/validateReview', views.validateReview),
    url(r'^/logout', views.logout),
    url(r'^$', views.books)
]