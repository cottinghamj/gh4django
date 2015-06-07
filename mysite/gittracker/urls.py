from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.setup, name='index'),
    url(r'^add/$', views.addFile, name='addFile'),
    url(r'^rent/$', views.rentFile, name='rentFile'),
    url(r'^return/$', views.returnFile, name='returnFile'),


#  url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
]

