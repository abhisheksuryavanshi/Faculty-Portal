from django.contrib.auth.models import Permission, User
from django.db import models


class Bio(models.Model):
    user = models.ForeignKey(User, default=1)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    designation = models.CharField(max_length=500)
    institute_name = models.CharField(max_length=100)
    profile_photo = models.FileField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + ' - ' + self.last_name

class Office_details(models.Model):
	user = models.ForeignKey(User, default=1)
	room_no = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20)
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.room_no

class Work_experience(models.Model):
	user = models.ForeignKey(User, default=1)
	job_post = models.CharField(max_length=100)
	job_experience = models.CharField(max_length=100)
	job_place = models.CharField(max_length=100)
	job_start = models.CharField(max_length=50)
	job_end = models.CharField(max_length=50)

	def __str__(self):
		return self.job_post + ', ' + self.job_place

class Research_interests(models.Model):
	user = models.ForeignKey(User, default=1)
	research_area = models.CharField(max_length=200)

	def __str__(self):
		return self.research_area