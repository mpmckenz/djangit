from django.db import models

from django.contrib.auth.models import User


class DjangitUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    subscriptions = models.ManyToManyField(
        'djangit.Subdjangit', symmetrical=False, blank=True, related_name='subscriptions')
    moderator = models.ManyToManyField(
        'djangit.Subdjangit', blank=True, related_name='moderator')

    def __str__(self):
        return self.username

# views.py
# Django built-in permissions: create, change, delete
# djangit.delete_post???
# 'djangit.change_post'

# check permission
