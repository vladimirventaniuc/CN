from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^uploadfile/',views.upload,name='upload'),
    url(r'^getfile/',views.getFile,name='getFile'),
]