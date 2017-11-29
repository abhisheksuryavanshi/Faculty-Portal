from django.contrib.auth.models import Permission, User
from django.db import models


class Achievements(models.Model):
    user = models.ForeignKey(User, default=1)
    achievement = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username