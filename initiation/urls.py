from django.conf.urls import url
from . import views

urlpatterns = [
    #path('accueil', views.home),
    #path('', views.home),
    url(r'^$', views.index, name='index'),
]