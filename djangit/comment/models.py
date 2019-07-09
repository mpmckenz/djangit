from django.db import models
from djangit.user.models import DjangitUser
from djangit.post.models import Post
import datetime


class Comment(models.Model):
    user = models.ForeignKey(DjangitUser, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(
        DjangitUser, related_name="commentupvotes", blank=True)
    downvotes = models.ManyToManyField(
        DjangitUser, related_name="commentdownvotes", blank=True)

    def get_score(self):
        return self.upvotes.count() - self.downvotes.count()