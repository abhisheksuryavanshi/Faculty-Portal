from django.shortcuts import render
from homepage.models import Bio
from accounts.models import Teaching
from achievements.models import Achievements
from publications.models import Publication
from django.contrib.auth.models import Permission, User
from infop.models import Info

def index(request,user_name):
	tobeseenuser = User.objects.get(username=user_name)
	bio = Info.objects.filter(user=tobeseenuser)
	context = {
		'anshp': bio,
		'username': user_name
		}
	return render(request, 'viewonly/index.html',context)

def achievements(request,user_name):
	tobeseenuser = User.objects.get(username=user_name)
	achievements = Achievements.objects.filter(user=tobeseenuser)
	bio = Info.objects.filter(user=tobeseenuser)
	context = {
		'anshp': bio,
		'achievements': achievements,
		'username': user_name
		}
	return render(request, 'viewonly/achievements.html',context)

def teachings(request,user_name):
	tobeseenuser = User.objects.get(username=user_name)
	teachings = Teaching.objects.filter(user=tobeseenuser)
	bio = Info.objects.filter(user=tobeseenuser)
	context = {
		'anshp': bio,
		'teachings': teachings,
		'username': user_name
		}	
	return render(request, 'viewonly/teachings.html', context)

def publications(request,user_name):
	tobeseenuser = User.objects.get(username=user_name)
	publications = Publication.objects.filter(user=tobeseenuser)
	bio = Info.objects.filter(user=tobeseenuser)
	context = {
		'anshp': bio,
		'publications': publications,
		'username': user_name
		}	
	return render(request, 'viewonly/publications.html', context)

