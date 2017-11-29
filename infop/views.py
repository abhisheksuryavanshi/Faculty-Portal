from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Info
from homepage.models import Office_details, Work_experience, Research_interests



def index(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')

    else:
        ansh = Info.objects.filter(user=request.user)
        office_details = Office_details.objects.filter(user=request.user)
        work_experience = Work_experience.objects.filter(user=request.user)
        research_interests = Research_interests.objects.filter(user=request.user)
        return render(request, 'infop/index.html', {'anshp': ansh,
                                                    'office_details':office_details,
                                                    'work_experience':work_experience,
                                                    'research_interests':research_interests
                                                    })

def save(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        if request.method == "POST" or None or request.method == "FILES" or None:
            aa = Info.objects.get(user=request.user)
            aa.dept = request.POST['dept']
            aa.username = request.POST['username']
            aa.email = request.POST['email']
            aa.first_name = request.POST['first_name']
            aa.last_name = request.POST['last_name']
            aa.designation = request.POST['designation']
            aa.institute_name = request.POST['institute_name']
            aa.phone_number = request.POST['phone_number']
            aa.p_photo = request.FILES['profile_photo']
            aa.about = request.POST['about']
            aa.link = request.POST['link']

            aa.save()
            ansh=Info.objects.filter(user=request.user)
            office_details = Office_details.objects.filter(user=request.user)
            work_experience = Work_experience.objects.filter(user=request.user)
            research_interests = Research_interests.objects.filter(user=request.user)

            return render(request, 'infop/index.html', {'anshp': ansh,
                                                    'office_details':office_details,
                                                    'work_experience':work_experience,
                                                    'research_interests':research_interests
                                                    })
def delete_teaching(request, we_id):
    tobedeleted = Work_experience.objects.get(pk=we_id)
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
