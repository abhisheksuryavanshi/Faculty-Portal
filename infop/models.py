from django.contrib.auth.models import Permission, User
from django.db import models

class Info(models.Model):
    user = models.ForeignKey(User, default=1)
    dept = models.CharField(max_length= 100 , default='dept')
    username = models.CharField(max_length=100 , default='username')
    email = models.CharField(max_length=100,default='EMAIL')
    first_name = models.CharField(max_length=250 , default='FIRST_NAME')
    last_name = models.CharField(max_length=100 , default='LAST_NAME')
    designation = models.CharField(max_length=500 , default='Designation')
    institute_name = models.CharField(max_length=100 , default='Institute')
    p_photo = models.FileField(upload_to='media', default='12.jpg',blank=True)
    phone_number = models.CharField(max_length=20 , default='999999999')
    about = models.CharField(max_length=500 , default='I am me')
    link = models.CharField(max_length=1000, default='#')

    def __str__(self):
        return self.username + ' - ' + self.email