from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
import json
import urllib
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import File
from .forms import FileForm

def index(request):
	f=open("abc.txt", "r")
	contents =f.read()
	f.close()
	return render(request,'fileread/main.html',{'content': contents})
	