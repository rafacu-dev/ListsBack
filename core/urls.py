import re
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static, serve

from django.conf import settings

def staticProduction(prefix, view=serve, **kwargs):
    if settings.DEBUG:
        return []
    return [
        re_path(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs),
    ]



urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),

    path('user/', include('user.urls')),
    path('lists/', include('user.lists')),
    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticProduction(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
