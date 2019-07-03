from django.db import models

from django.contrib.auth.models import User, Group


class DjangitUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    following = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False, blank=True)
    moderator = models.OneToManyField(
        Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user
