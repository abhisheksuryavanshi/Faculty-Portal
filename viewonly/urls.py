from django.conf.urls import url ,include
from . import views

app_name = 'viewonly'

urlpatterns = [
	url(r'^(?P<user_name>[a-zA_Z]+)/$', views.index, name='index'),
	url(r'^(?P<user_name>[a-zA-Z]+)/to_homepage$', views.index, name='to_homepage'),
	url(r'^(?P<user_name>[a-zA_Z]+)/to_achievements/$', views.achievements, name='to_achievements'),
	url(r'^(?P<user_name>[a-zA_Z]+)/to_teachings/$', views.teachings, name='to_teachings'),
	url(r'^(?P<user_name>[a-zA_Z]+)/to_publications/$', views.publications, name='to_publications'),
	]
