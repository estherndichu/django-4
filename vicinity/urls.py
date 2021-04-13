import os
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views


urlpatterns = [
    url('',views.index,name='index'),
    url('^new_vicinity/',views.new_vicinity)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)