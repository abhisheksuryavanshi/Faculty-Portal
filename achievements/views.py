from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import AchievementsForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Achievements
from infop.models import Info
import requests
from bs4 import BeautifulSoup

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        achnts = Achievements.objects.filter(user=request.user)
        bio = Info.objects.filter(user=request.user)
        return render(request, 'achievements/index.html', {'anshp': bio,'achievements': achnts})

def logoutss(request):
    logout(request)
    return render(request, 'accounts/login.html')

def create_achievement(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        form = AchievementsForm(request.POST or None)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.user = request.user                                  
            achievement.save()
            achievements = Achievements.objects.filter(user=request.user)
            return render(request, 'achievements/index.html', {'achievements': achievements})
        context = {
            "form": form,
        }
        return render(request, 'achievements/add_achievement.html', context)

def delete_achievement(request, ach_id):
    tobedeleted = Achievements.objects.get(pk=ach_id)
    tobedeleted.delete()
    achievements = Achievements.objects.filter(user=request.user)
    return render(request, 'achievements/index.html', {'achievements': achievements})


def edit_achievement(request, ach_id):
    tobeedited = Achievements.objects.get(pk=ach_id)
    Achievements.objects.get(pk=ach_id).delete()
    return render(request, 'achievements/add_achievement.html', {'tobeedited': tobeedited , 'error':'aaa'})


def searched_achievements(request):
    achievements = Achievements.objects.filter(user=request.user)
    searched_achievement = request.POST['search1']
    context = {
        'achievements': achievements,
        'searched_achievement': searched_achievement,
    }
    return render(request, 'achievements/searched_achievements.html', context)

def loaddata(request):
    linkobj = Info.objects.filter(user=request.user).first()

    url = linkobj.link

    dic = {}

    res = []

    r  = requests.get(url)

    data = r.text

    # soup = BeautifulSoup(data,'lxml')
    soup = BeautifulSoup(data)

    main = soup.find("div",{ "id" : "fh5co-main" })

    content = soup.find("div",{ "data-content" : "7" })

    ul = content.find("ul")

    publications = ul.find_all("li")

    for item in publications :
        te = item.text

        publ = Achievements.objects.create()

        publ.user = request.user

        publ.achievement = te

        publ.save()

    publiions = Achievements.objects.filter(user=request.user)
    return render(request, 'achievements/index.html', {'achievements': publiions})