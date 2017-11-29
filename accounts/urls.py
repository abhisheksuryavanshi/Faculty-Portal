from django.conf.urls import url, include
from . import views
from homepage import views as homepage_views
from django.contrib.auth.views import password_reset , password_reset_done, password_reset_confirm

app_name = 'accounts'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^create_teaching/$', views.create_teaching, name='create_teaching'),
    url(r'^logout/$', views.logoutss, name='logout'),
    url(r'^admin/$', views.dummy, name='admin'),
    # url(r'^verified-email-field/', include('verified_email_field.urls')),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
    #     name='activate'),
    url(r'^(?P<teaching_id>[0-99]+)/delete_teaching/$', views.delete_teaching, name='delete_teaching'),
    url(r'^addimage/$', views.addimage, name='addimage'),
    url(r'^to_homepage/$', homepage_views.index, name='to_homepage'),
    url(r'^(?P<teaching_id>[0-99]+)/set_previous/$', views.set_previous, name='set_previous'),
    url(r'^searched_user/$', views.searched_user, name='searched_user'),
    url(r'^listall/$', views.listall, name='listall'),
    url(r'^send/$', views.send, name='send'),
	url(r'^messaging/$', views.messaging, name='messaging'),
    url(r'^message/$', views.message, name='message'),
    url(r'^(?P<message_id>[0-99]+)/delete_messages/$', views.delete_messages, name='delete_messages'),
    url(r'^ldtea$', views.loaddata, name='ldtea'),
    # url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^reset_password/$', password_reset, name='reset_password'),
    url(r'^reset_password_done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^login/$', views.login_user, name='login_user'),
]
