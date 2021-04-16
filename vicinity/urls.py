import os
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('new_vicinity/',views.new_vicinity, name='new_vicinity'),
    path("profile/", views.profile, name="profile"),
    path('update_profile/',views.update_profile,name = 'update_profile'),
    path('join/<id>', views.join, name='join'),
    path('leave/<id>', views.leave, name='leave'),
    path('single_hood/<hood_id>', views.single_hood, name='single-hood'),
    path('business/', views.business, name='business'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)