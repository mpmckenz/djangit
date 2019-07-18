from django.db import models
from django.utils import timezone

from djangit.user.models import DjangitUser


class Subdjangit(models.Model):
    moderator = models.ForeignKey(
        'djangit.DjangitUser', on_delete=models.CASCADE, related_name='moderator')
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50, default="")
    about = models.TextField(max_length=75, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
