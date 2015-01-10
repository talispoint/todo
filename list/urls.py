from django.conf.urls import patterns, url
from list import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^finished/(?P<todo_id>\d+)/$', views.finished, name='finished'),
)