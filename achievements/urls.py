from django.conf.urls import url, include
from . import views
from accounts import views as accounts_views
from homepage import views as homepage_views

app_name = 'achievements'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='to_achievements'),
    url(r'^logout/$', views.logoutss, name='logout'),
    url(r'^create_achievement/$', views.create_achievement, name='create_achievement'),
    url(r'^(?P<ach_id>[0-99]+)/delete_achievement/$', views.delete_achievement, name='delete_achievement'),
    url(r'^(?P<ach_id>[0-99]+)/edit_achievement/$', views.edit_achievement, name='edit_achievement'),
    url(r'^to_homepage/$', homepage_views.index, name='to_homepage'),
    url(r'^ldach$', views.loaddata, name='ldach'),
    url(r'^searched_achievements/$', views.searched_achievements, name='searched_achievements'),
]
