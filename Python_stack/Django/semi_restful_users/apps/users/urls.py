from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'(?P<number>\d+)$', views.display),
    url(r'(?P<number>\d+)/edit$', views.edit),
    url(r'(?P<number>\d+)/update$', views.update),
    url(r'(?P<number>\d+)/delete$', views.delete),
    url(r'new$', views.new),
    url(r'create$', views.create),    
]