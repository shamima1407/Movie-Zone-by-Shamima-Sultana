from django.contrib import admin
from django.urls import path, include, re_path
#from django.conf.urls import url, include
from django.conf.urls import include

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^home/', include('home.urls')),
    re_path(r'^reg/', include('reg.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
