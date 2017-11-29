from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
import json
import urllib
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .forms import PublicationForm
from .models import Publication
from infop.models import Info
from bs4 import BeautifulSoup
import requests


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        publications = Publication.objects.filter(user=request.user)
        bio = Info.objects.filter(user=request.user)
        return render(request, 'publications/index.html', {'anshp': bio,'publications': publications})


def logoutss(request):
    logout(request)
    return render(request, 'accounts/login.html')


def create_publication(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        form = PublicationForm(request.POST or None)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.user = request.user
            publication.save()
            publications = Publication.objects.filter(user=request.user)
            return render(request, 'publications/index.html', {'publications': publications})
        context = {
            "form": form,
        }
        return render(request, 'publications/add_publication.html', context)


def edit_publication(request, publication_id):
    tobeedited = Publication.objects.get(pk=publication_id)
    Publication.objects.get(pk=publication_id).delete()
    return render(request, 'publications/add_publication.html', {'tobeedited': tobeedited , 'error':'aaa'})


def delete_publication(request, publication_id):
    tobedeleted = Publication.objects.get(pk=publication_id)
    tobedeleted.delete()
    publications = Publication.objects.filter(user=request.user)
    return render(request, 'publications/index.html', {'publications': publications})


def searched_publications(request):
    publications = Publication.objects.filter(user=request.user)
    searched_publication = request.POST['search']
    context = {
        'publications': publications,
        'searched_publication': searched_publication,
    }
    return render(request, 'publications/searched_publications.html', context)


def loaddata(request):
    linkobj = Info.objects.filter(user=request.user).first()

    url = linkobj.link

    dic = {}

    res = []

    r = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data,'lxml')

    # soup = BeautifulSoup(data, 'lxml')

    main = soup.findAll("div", {"id": "fh5co-main"})

    content = soup.find("div", {"data-content": "5"})

    # heading = content.find("h4")

    # sp = heading.text.split("\n")

    ul = content.find("ul")

    publications = ul.find_all("li")

    for item in publications :
        te = item.text

        publ = Publication.objects.create()

        publ.user = request.user

        publ.publication = te

        publ.save()

    publiions = Publication.objects.filter(user=request.user)
    return render(request, 'publications/index.html', {'publications': publiions})



