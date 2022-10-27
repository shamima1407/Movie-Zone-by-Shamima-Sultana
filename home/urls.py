from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^home', views.index, name='index'),
    re_path(r'^action', views.action, name='action'),
    re_path(r'^bangla', views.bangla, name='bangla'),   
    re_path(r'^single', views.single, name='single'),
    re_path(r'^list', views.list, name='list'),
]