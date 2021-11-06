from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^home', views.index, name='index'),
    url(r'^action', views.action, name='action'),

    url(r'^bangla', views.bangla, name='bangla'),
    
    url(r'^single', views.single, name='single'),

    url(r'^list', views.list, name='list'),
]