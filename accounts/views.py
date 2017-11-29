from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import AddTeachingForm,UserForm,AddProfilePhoto
import json
import urllib
from django.conf import settings
from .models import Teaching,Image,Mailing
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from homepage.models import Bio
from infop.models import Info
import datetime
import requests
from bs4 import BeautifulSoup

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        teachings = Teaching.objects.filter(user=request.user)
        bio = Info.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            teachings = teachings.filter(
                Q(coursename__icontains=query) |
                Q(startyear__icontains=query)
            ).distinct()
            return render(request, 'accounts/index.html', {
                'anshp': bio,
                'teachings': teachings,
            })
        else:
            return render(request, 'accounts/index.html', {'anshp': bio,'teachings': teachings})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                ansh=Info.objects.filter(user=request.user)
                return render(request, 'infop/index.html', {'anshp': ansh})
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})
    return render(request, 'accounts/login.html')


def create_teaching(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        form = AddTeachingForm(request.POST or None)
        if form.is_valid():
            teaching = form.save(commit=False)
            teaching.user = request.user                                  

            teaching.save()
            teaings = Teaching.objects.filter(user=request.user)
            return render(request, 'accounts/index.html', {'teachings': teaings})
            # change index.html here to details.html
        
        context = {
            "form": form,
        }
        
        return render(request, 'accounts/add_teaching.html', context)


# def register(request):
#     if request.method == "POST":
#
#         form = UserForm(request.POST or None)
#         if form.is_valid():
#             user = form.save(commit=False)
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             password1 = form.cleaned_data['password1']
#
#             ''' Begin reCAPTCHA validation '''
#             recaptcha_response = request.POST.get('g-recaptcha-response')
#             url = 'https://www.google.com/recaptcha/api/siteverify'
#             values = {
#                 'secret': "6LdOmjcUAAAAAF1dXs-eIVwrygU-Ii7Eyo7pcggk",
#                 'response': recaptcha_response
#             }
#             data = urllib.parse.urlencode(values).encode()
#             req = urllib.request.Request(url, data=data)
#             response = urllib.request.urlopen(req)
#             result = json.loads(response.read().decode())
#             ''' End reCAPTCHA validation '''
#
#             if password == password1 and result['success']:
#                 object = Mailing.objects.create(teacher=username, date=datetime.datetime.now())
#                 objecct1 = Info.objects.create(username=username)
#                 user.set_password(password)
#                 user.last_name = "0"
#                 user.first_name = "0"
#                 user.is_active = False
#                 user.save()
#                 current_site = get_current_site(request)
#                 message = render_to_string('accounts/acc_active_email.html', {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 })
#                 mail_subject = 'Activate your account.'
#                 to_email = form.cleaned_data.get('email')
#                 email = EmailMessage(mail_subject, message, to=[to_email])
#                 email.send()
#                 return HttpResponse('Please confirm your email address to complete the registration')
#                     # user = authenticate(username=username, password=password)
#                     # if user is not None:
#                     #     if user.is_active:
#                     #         login(request, user)
#                     #         teachings = Teaching.objects.filter(user=request.user)
#                     #         return render(request, 'accounts/index.html', {'teachings': teachings})
#             elif password != password1:
#                 return render(request, 'accounts/login.html', {'error_message': 'Password dont match '})
#         return render(request, 'accounts/login.html', {'error_message': 'Invalid Email or No Captcha'})


def register(request):
    if request.method == "POST":

        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password1 = form.cleaned_data['password1']


            if password == password1:
                user.set_password(password)
                user.last_name = "0"
                user.first_name = "0"
                user.is_active = True
                user.save()
                login(request, user)
                object = Mailing.objects.create(teacher=username, date=datetime.datetime.now())
                object1 = Info.objects.create()
                object1.user = request.user
                object1.username = username
                object1.save()
                anshp = Info.objects.filter(username=request.user.username)
                return render(request, 'infop/index.html', {'anshp': anshp})

            elif password != password1:
                return render(request, 'accounts/login.html', {'error_message': 'Password dont match '})
        return render(request, 'accounts/login.html', {'error_message': 'Invalid Email or No Captcha'})


def logoutss(request):
    logout(request)
    return render(request, 'accounts/login.html')

def dummy(request):
    return

# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#
#         user.save()
#
#         login(request, user)
#         object = Info.objects.create(user=request.user)
#         # return redirect('home')
#         teachings = Teaching.objects.filter(user=request.user)
#         anshp= Info.objects.filter(user=request.user)
#         return render(request, 'infop/index.html', {'anshp': anshp})
#     else:
#         return HttpResponse('Activation link is invalid!')

def delete_teaching(request, teaching_id):
    tobedeleted = Teaching.objects.get(pk=teaching_id)
    tobedeleted.delete()
    teachings = Teaching.objects.filter(user=request.user)
    return render(request, 'accounts/index.html', {'teachings': teachings})

def addimage(request):
    teachings = Teaching.objects.filter(user=request.user)
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        form = AddProfilePhoto(request.POST or None, request.FILES or None)
        if form.is_valid():
            photo = form.save(commit=false)
            photo.user = request.user
            photo.profile_photo = request.FILES['profile_photo']
            photo.save()
            context = {
            'form':form,
            'teachings': teachings,
            'image': photo,
            }
            return render(request, 'accounts/index.html',context)
    return render(request, 'accounts/index.html',{'teachings': teachings})

def listall(request):
    users = User.objects.all()
    profiles = Info.objects.all()
    context = {
        'users': users,
        'profiles': profiles,
    }
    return render(request, 'accounts/listall.html',context)

def searched_user(request):
    users = User.objects.all()
    searched_user = request.POST['user_name']
    context = {
        'users': users,
        'searched_user': searched_user,
    }
    return render(request, 'accounts/searched_user.html',context)

def set_previous(request, teaching_id):
    tobeedited = Teaching.objects.get(pk=teaching_id)
    tobedeleted = Teaching.objects.get(pk=teaching_id)
    tobedeleted.delete()
    tobeedited.is_ongoing=False
    tobeedited.save()
    teachings = Teaching.objects.filter(user=request.user)
    return render(request, 'accounts/index.html', {'teachings': teachings})


def messaging(request):
    mails = Mailing.objects.filter(teacher=request.user.username)
    USER = User.objects.get(username=request.user)
    if not USER.first_name == USER.last_name:
        diff = int(USER.last_name) - int(USER.first_name)
        USER.last_name = USER.first_name
        USER.save()
        return render(request, 'accounts/messaging.html', {'mails': mails , 'error_message2': 'You have '+str(diff)+' new messages', 'diff':diff})
    else:
        return render(request,'accounts/messaging.html', {'mails': mails})


def message(request):
    mails = Mailing.objects.filter(teacher=request.user.username)
    USER = User.objects.get(username=request.user)
    to = request.POST['mssg_id']
    if not USER.first_name == USER.last_name:
        diff = int(USER.last_name) - int(USER.first_name)
        USER.last_name = USER.first_name
        USER.save()
        return render(request, 'accounts/messaging.html', {'mails': mails , 'error_message2': 'You have '+str(diff)+' new messages', 'to': to, 'diff': diff})
    else:
        return render(request,'accounts/messaging.html', {'mails': mails, 'to': to})


def send(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        mails = Mailing.objects.filter(teacher=request.user.username)
        USER = User.objects.filter(username=request.user)
        if request.POST['to'] and request.POST['send']:
            to = request.POST['to']
            sends = request.POST['send']
            # userd = request.user
            if str(to) == "all":
                users = User.objects.all()
                for user in users:
                    if not user == request.user :
                        Mailing.objects.create(teacher=user.username, sender=request.user, inbox=sends, date=datetime.datetime.now())
                        user.last_name = str(int(user.last_name) + 1)
                        user.save()
                return render(request, 'accounts/messaging.html', {'mails': mails})

            else:
                count = User.objects.filter(username=str(to)).count()
                if int(count) == 0:
                    return render(request, 'accounts/messaging.html',{'mails': mails, 'error_message': 'Enter a valid Username'})
                else:
                    # logout(request)
                    user = User.objects.get(username=str(to))

                    user.last_name = str(int(user.last_name) + 1)
                    user.save()

                    # login(request, user)

                    Mailing.objects.create(teacher=user.username , sender=request.user , inbox=sends, date=datetime.datetime.now())
                    # logout(request)

                    # login(request, userd)

                    return render(request, 'accounts/messaging.html', {'mails': mails})
        else:
            return render(request, 'accounts/messaging.html', {'mails': mails, 'error_message': 'Fill both fields'})


def delete_messages(request, message_id):
    tobedeleted = Mailing.objects.get(pk=message_id)
    tobedeleted.delete()
    mails = Mailing.objects.filter(teacher=request.user)
    return render(request, 'accounts/message1.html', {'mails': mails})



def loaddata(request):
    linkobj = Info.objects.filter(user=request.user).first()

    url = linkobj.link

    dic = {}

    res = []

    r  = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data,'lxml')

    main = soup.find("div",{ "id" : "fh5co-main" })

    content = soup.find("div",{ "data-content" : "2" })

    ul = content.find("ul")

    publications = ul.find_all("li")

    for item in publications :

        sp = item.text.split("&")#start year at index 0
        name = sp[1].split("; ")#coursename at index 1
        ab = sp[2].split("; ")#sem name at index 1
        yr = sp[0].split(" ")
        z = yr[1].split("-")
        print(z[0])     #YEAR
        print(name[1])  #SEMNAME
        print(ab[1])    #COURSENAME
        publ = Teaching.objects.create()

        publ.user = request.user

        publ.coursename = ab[1]

        publ.start_year = z[0]

        if name[1] == "Even Semester":
            publ.start_month = "August"
        else:
            publ.start_month = "January"

        publ.teacher_name = str(linkobj.first_name) + ' ' + str(linkobj.last_name)

        publ.is_ongoing = True

        publ.save()

    publiions = Teaching.objects.filter(user=request.user)
    return render(request, 'accounts/index.html', {'teachings': publiions})