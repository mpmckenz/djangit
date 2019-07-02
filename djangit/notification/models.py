from django.db import models
from djangit.post.models import Post
from djangit.user.models import DjangitUser


class Notification(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    notify_user = models.ForeignKey(DjangitUser, on_delete=models.CASCADE)
    noticed = models.BooleanField(default=False)
