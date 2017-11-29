from django.contrib.auth.models import Permission, User
from django.db import models
import datetime


# Create your models here.

class Teaching(models.Model):
    user = models.ForeignKey(User, default=1)
    coursename = models.CharField(max_length=250)
    start_month = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    is_ongoing = models.BooleanField(default=True)
    teacher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.coursename + ' - ' + self.start_year


class Image(models.Model):
    user = models.ForeignKey(User, default=1)
    profile_photo = models.FileField()


class Mailing(models.Model):
    teacher = models.CharField(max_length=100, default=1)
    sender = models.CharField(max_length=100, default="ADMIN")
    inbox = models.CharField(max_length=10000, default="Welcome to Our website")
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.teacher
