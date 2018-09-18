from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^edit', views.edit),
    url(r'^add$', views.add),
    url(r'^addUser', views.addUser),
    url(r'^processing', views.processing),
    url(r'^delete', views.delete),
    url(r'^', views.index)
]
