from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/', views.about, name='about')
                        )

# For section 4.7 Exercise
# Creating an about page with a link back to the main index page
#urlpatterns = patterns('',
#                       url(r'^$', views.index, name='index'),
#                       url(r'^about/', views.about, name='about')
#                        )
