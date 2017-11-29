from django.conf.urls import url ,include
from . import views
from accounts import views as accounts_views
from achievements import views as achievements_views
from publications import views as publications_views

app_name = 'homepage'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^logout/$', views.logoutss, name='logout'),
	url(r'^create_bio/$', views.create_bio, name='create_bio'),
	url(r'^create_office_details/$', views.create_office_details, name='create_office_details'),
	url(r'^create_research_interests/$', views.create_research_interests, name='create_research_interests'),
	url(r'^create_work_experience/$', views.create_work_experience, name='create_work_experience'),
	url(r'^(?P<bio_id>[0-99]+)/delete_bio/$', views.delete_bio, name='delete_bio'),
	url(r'^to_teaching/$', accounts_views.index, name='to_teaching'),
	url(r'^to_achievements/$', achievements_views.index, name='to_achievements'),
	url(r'^to_publications/$', publications_views.index, name='to_publications'),
	url(r'^(?P<office_id>[0-99]+)/delete_office/$', views.delete_office, name='delete_office'),
	url(r'^(?P<office_id>[0-99]+)/delete_office/$', views.delete_office, name='delete_teaching'),
	url(r'^(?P<work_id>[0-99]+)/delete_work/$', views.delete_work, name='delete_work'),
	url(r'^(?P<research_id>[0-99]+)/delete_research/$', views.delete_research, name='delete_research'),
	]



	