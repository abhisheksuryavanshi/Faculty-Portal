from django import forms
from django.contrib.auth.models import User

from .models import Bio, Office_details, Work_experience, Research_interests


class BioForm(forms.ModelForm):

    class Meta:
        model = Bio
        fields = ['first_name', 'last_name', 'designation', 'institute_name', 'profile_photo', 'phone_number']

class Office_detailsForm(forms.ModelForm):

    class Meta:
        model = Office_details
        fields = [  'room_no', 'phone_number', 'email']

class Work_experienceForm(forms.ModelForm):

    class Meta:
        model = Work_experience
        fields = [	'job_post', 'job_experience',
        			'job_place', 'job_start', 'job_end']

class Research_interestsForm(forms.ModelForm):

    class Meta:
        model = Research_interests
        fields = [	'research_area' ]