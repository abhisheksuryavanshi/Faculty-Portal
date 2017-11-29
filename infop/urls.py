from django.conf.urls import url
from . import views
from homepage import views as homepage_views
from accounts import views as accounts_views

app_name = 'infop'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^save/$', views.save, name='save'),
    url(r'^to_teaching/$', accounts_views.index, name='to_teaching'),
    url(r'^to_homepage/$', homepage_views.index, name='to_homepage'),
]
