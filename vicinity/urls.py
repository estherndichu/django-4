import os
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$',views.index,name='index'),
    url('^new_vicinity/',views.new_vicinity, name='new_vicinity'),
    url("^profile/", views.profile, name="profile"),
    url('^update_profile/',views.update_profile,name = 'update_profile'),
    url('join/<id>', views.join, name='join'),
    url('leave/<id>', views.leave, name='leave'),
    url('single_hood/<hood_id>', views.single_hood, name='single-hood'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)