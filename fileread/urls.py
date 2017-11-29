from django.conf.urls import url ,include
from . import views
from accounts import views as accounts_views
from homepage import views as homepage_views

app_name = 'fileread'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	
	]