from django.db import models
from vote.models import VoteModel
from djangit.user.models import DjangitUser


class Post(VoteModel, models.Model):
    user = models.ForeignKey(DjangitUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200)
    # total_votes = models.IntegerField(default=0)
    # upvotes = models.IntegerField(default=0)
    # downvotes = models.IntegerField(default=0)

    def get_score(self):
        return self.upvotes - self.downvotes
