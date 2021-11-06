from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
#    url(r'^reg/', include('reg.urls')),
    url(r'^reg/', views.registration, name='registration'),
    url(r'^log/', views.login, name='login'),
    url(r'^msg/', views.msg, name='msg'),
    url(r'^error/', views.error, name='error'),
    
]