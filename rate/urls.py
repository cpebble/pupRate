from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from rate import views

urlpatterns = [
    url(r'^about/', views.about, name = "about"),
    url(r'^rate/', views.rate, name="rate"),
    url(r'^pup/$', views.pup, name="rate"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    url(r'^pup/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),

]
