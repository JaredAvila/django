from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^recipe/view', views.viewRecipe),
    url(r'^registration', views.registration),
    url(r'^validate/login', views.validateLogin),
    url(r'^validate/registration', views.validateReg),
    url(r'^validate/recipe', views.validateRecipe),
    url(r'^validate/likes', views.validateRecipe),
    url(r'^validate/comment', views.validateComment),
    url(r'^edit/recipe', views.editRecipe),
    url(r'^editting/recipe', views.edit),
    url(r'^delete/recipe', views.deleteRecipe),
    url(r'^delete/comment', views.deleteComment),
    url(r'^delete', views.delete),
    url(r'^home', views.home),
    url(r'^logout', views.logout),
    url(r'^login', views.login)
]
