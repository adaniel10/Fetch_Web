__author__ = 'Abin'

from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'))
urlpatterns = patterns('', url(r'^about/', views.about, name='about'))
