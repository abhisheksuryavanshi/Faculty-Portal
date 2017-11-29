from django import forms
from django.contrib.auth.models import User
from .models import Teaching,Image


class AddTeachingForm(forms.ModelForm):

    class Meta:
        model = Teaching
        fields = ['coursename', 'start_month', 'start_year', 'teacher_name','is_ongoing']

class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password' , 'password1']

class AddProfilePhoto(forms.ModelForm):

		class Meta:
			model = Image
			fields = ['profile_photo']
# class SongForm(forms.ModelForm):

#     class Meta:
#         model = Song
#         fields = ['song_title', 'audio_file']


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
