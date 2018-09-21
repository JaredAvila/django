from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.create),
    url(r'^all.json', views.allJSON),
    url(r'^all.html', views.allHTML),
    url(r'^find$', views.find),
    url(r'^', views.index)
]
