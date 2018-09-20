from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^checkout', views.checkout),
    url(r'^confirm', views.confirm),
    url(r'^', views.index)
]
