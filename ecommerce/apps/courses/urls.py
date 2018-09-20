from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/confirm', views.confirm),
    url(r'^/delete', views.delete),
    url(r'^/processing', views.processing),
    url(r'^$', views.index)
]
