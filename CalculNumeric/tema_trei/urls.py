from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^check/',views.check,name='check'),
    url(r'^upload/',views.upload,name='upload'),
    url(r'^getSum/',views.getSum,name='getSum'),
    url(r'^getProd/',views.getProd,name='getProd'),
]