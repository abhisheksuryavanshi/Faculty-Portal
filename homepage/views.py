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
from .forms import BioForm, Office_detailsForm, Research_interestsForm, Work_experienceForm
from .models import Bio, Office_details, Research_interests, Work_experience
from infop.models import Info

def index(request):

    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        bio = Bio.objects.filter(user=request.user)
        return render(request, 'homepage/index.html', {'bio': bio})

def logoutss(request):
    logout(request)
    return render(request, 'accounts/login.html')

def create_bio(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        form = BioForm(request.POST or None, request.FILES or None	)
        if form.is_valid():
            bio = form.save(commit=False)
            bio.user = request.user                                  
            bio.profile_photo = request.FILES['profile_photo']
            bio.save()
            bio = Bio.objects.filter(user=request.user)
            return render(request, 'homepage/index.html', {'bio': bio})
        context = {
            "form": form,
        }
        return render(request, 'homepage/add_bio.html', context)

def delete_bio(request, bio_id):
    tobedeleted = Bio.objects.get(pk=bio_id)
    tobedeleted.delete()
    bio = Bio.objects.filter(user=request.user)
    return render(request, 'homepage/index.html', {'bio': bio})


def create_work_experience(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        form = Work_experienceForm(request.POST or None, request.FILES or None  )
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.user = request.user                                  
            work_experience.save()
            ansh=Info.objects.filter(user=request.user)
            office_details = Office_details.objects.filter(user=request.user)
            work_experience = Work_experience.objects.filter(user=request.user)
            research_interests = Research_interests.objects.filter(user=request.user)

            return render(request, 'infop/index.html', {'anshp': ansh,
                                                    'office_details':office_details,
                                                    'work_experience':work_experience,
                                                    'research_interests':research_interests
                                                    })
        context = {
            "form": form,
        }
        return render(request, 'homepage/add_work_experience.html', context)

def create_office_details(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        form = Office_detailsForm(request.POST or None, request.FILES or None  )
        if form.is_valid():
            office_details = form.save(commit=False)
            office_details.user = request.user                                  
            office_details.save()
            ansh=Info.objects.filter(user=request.user)
            office_details = Office_details.objects.filter(user=request.user)
            work_experience = Work_experience.objects.filter(user=request.user)
            research_interests = Research_interests.objects.filter(user=request.user)

            return render(request, 'infop/index.html', {'anshp': ansh,
                                                    'office_details':office_details,
                                                    'work_experience':work_experience,
                                                    'research_interests':research_interests
                                                    })
        context = {
            "form": form,
        }
        return render(request, 'homepage/add_office_details.html', context)

def create_research_interests(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        form = Research_interestsForm(request.POST or None, request.FILES or None  )
        if form.is_valid():
            research_interests = form.save(commit=False)
            research_interests.user = request.user                                  
            research_interests.save()
            ansh=Info.objects.filter(user=request.user)
            office_details = Office_details.objects.filter(user=request.user)
            work_experience = Work_experience.objects.filter(user=request.user)
            research_interests = Research_interests.objects.filter(user=request.user)
            return render(request, 'infop/index.html', {'anshp': ansh,
                                                    'office_details':office_details,
                                                    'work_experience':work_experience,
                                                    'research_interests':research_interests
                                                    })
        context = {
            "form": form,
        }
        return render(request, 'homepage/add_research.html', context)

def delete_bio(request, bio_id):
    tobedeleted = Bio.objects.get(pk=bio_id)
    tobedeleted.delete()
    ansh=Info.objects.filter(user=request.user)
    office_details = Office_details.objects.filter(user=request.user)
    work_experience = Work_experience.objects.filter(user=request.user)
    research_interests = Research_interests.objects.filter(user=request.user)
    return render(request, 'infop/index.html', {'anshp': ansh,
                                            'office_details':office_details,
                                            'work_experience':work_experience,
                                            'research_interests':research_interests
                                            })

def delete_work(request, work_id):
    tobedeleted = Work_experience.objects.get(pk=work_id)
    tobedeleted.delete()
    ansh=Info.objects.filter(user=request.user)
    office_details = Office_details.objects.filter(user=request.user)
    work_experience = Work_experience.objects.filter(user=request.user)
    research_interests = Research_interests.objects.filter(user=request.user)
    return render(request, 'infop/index.html', {'anshp': ansh,
                                            'office_details':office_details,
                                            'work_experience':work_experience,
                                            'research_interests':research_interests
                                            })

def delete_office(request, office_id):
    tobedeleted = Office_details.objects.get(pk=office_id)
    tobedeleted.delete()
    ansh=Info.objects.filter(user=request.user)
    office_details = Office_details.objects.filter(user=request.user)
    work_experience = Work_experience.objects.filter(user=request.user)
    research_interests = Research_interests.objects.filter(user=request.user)
    return render(request, 'infop/index.html', {'anshp': ansh,
                                            'office_details':office_details,
                                            'work_experience':work_experience,
                                            'research_interests':research_interests
                                            })

def delete_research(request, research_id):
    tobedeleted = Research_interests.objects.get(pk=research_id)
    tobedeleted.delete()
    ansh=Info.objects.filter(user=request.user)
    office_details = Office_details.objects.filter(user=request.user)
    work_experience = Work_experience.objects.filter(user=request.user)
    research_interests = Research_interests.objects.filter(user=request.user)
    return render(request, 'infop/index.html', {'anshp': ansh,
                                            'office_details':office_details,
                                            'work_experience':work_experience,
                                            'research_interests':research_interests
                                            })
