import os
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url('^$',views.index,name='index'),
    url('new_vicinity/',views.new_vicinity, name='new_vicinity'),
    url("profile/", views.profile, name="profile"),
    url('update_profile/',views.update_profile,name = 'update_profile'),
    url('join/(\d+)', views.join, name='join'),
    url('leave/(\d+)', views.leave, name='leave'),
    url('single_hood/(\d+)', views.single_hood, name='single_hood'),
    url('business/(\d+)', views.business, name='business'),
    url('post/', views.post, name='post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)