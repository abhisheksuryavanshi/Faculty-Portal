from django.contrib.auth.models import Permission, User
from django.db import models


class Publication(models.Model):
    user = models.ForeignKey(User, default=1)
    publication = models.CharField(max_length=5000)

    def __str__(self):
        return self.user.username

