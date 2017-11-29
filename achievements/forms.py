from django import forms
from django.contrib.auth.models import User

from .models import Achievements


class AchievementsForm(forms.ModelForm):

    class Meta:
        model = Achievements
        fields = ['achievement']