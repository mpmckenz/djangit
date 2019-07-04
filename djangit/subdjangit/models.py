from django.db import models
from django.utils import timezone

from djangit.user.models import DjangitUser
from djangit.post.models import Post


class Subdjangit(models.Model):
    user = models.OneToOneField(DjangitUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    about = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    subscribers = models.ManyToManyField(DjangitUser, blank=True)
    # posts = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# sub.posts.objects.all()
# creator, title, about, subscribers, date?, subscribe option
# make new model about doing the posts, not comments
# veiws = will need get (subs) and post (valid? creator, title, about); subscribe button; all sub has subs, update, render; have filter option for your own; need function about posting; feed of recent;;; all subs and feed of posts; if subscribe, get post
# url = community
# choose comunity
