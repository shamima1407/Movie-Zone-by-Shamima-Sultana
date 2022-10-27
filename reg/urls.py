from django.urls import path, re_path
#from django.conf.urls import url, include
from django.conf.urls import include
from . import views

urlpatterns = [
#    url(r'^reg/', include('reg.urls')),
    re_path(r'^reg/', views.registration, name='registration'),
    re_path(r'^log/', views.login, name='login'),
    re_path(r'^msg/', views.msg, name='msg'),
    re_path(r'^error/', views.error, name='error'),
    
]