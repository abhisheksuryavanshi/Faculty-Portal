from django.contrib.auth.models import Permission, User
from django.db import models


class File(models.Model):
    user = models.ForeignKey(User, default=1)
    file = models.FileField()
