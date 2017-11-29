from django.conf.urls import url, include
from . import views
from accounts import views as accounts_views
from achievements import views as achievements_views
from homepage import views as homepage_views

app_name = 'publications'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logoutss, name='logout'),
    url(r'^create_publication/$', views.create_publication, name='create_publication'),
    url(r'^(?P<publication_id>[0-99]+)/delete_publication/$', views.delete_publication, name='delete_publication'),
    url(r'^(?P<publication_id>[0-99]+)/edit_publication/$', views.edit_publication, name='edit_publication'),
    url(r'^to_homepage/$', homepage_views.index, name='to_homepage'),
    url(r'^ld$', views.loaddata, name='ld'),
    url(r'^searched_publications/$', views.searched_publications, name='searched_publications'),
]
