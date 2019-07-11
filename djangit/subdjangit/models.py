from django.db import models
from django.utils import timezone

from djangit.user.models import DjangitUser
from djangit.post.models import Post


class Subdjangit(models.Model):
    creater = models.ForeignKey(DjangitUser, on_delete=models.CASCADE, null=True, related_name='creator')
    title = models.CharField(max_length=25, default='')
    about = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    subscribers = models.ManyToManyField(DjangitUser, related_name='subscribers', blank=True)
    

    def __str__(self):
        return self.title

# sub.posts.objects.all()
# creator, title, about, subscribers, date?, subscribe option
# make new model about doing the posts, not comments
# veiws = will need get (subs) and post (valid? creator, title, about); subscribe button; all sub has subs, update, render; have filter option for your own; need function about posting; feed of recent;;; all subs and feed of posts; if subscribe, get post
# url = community
# choose comunity
