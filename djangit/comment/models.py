from django.db import models
from djangit.user.models import DjangitUser
from django.utils import timezone
from djangit.post.models import Post



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=True, related_name='comments')
    user = models.ForeignKey(DjangitUser, on_delete=False)
    text = models.TextField(max_length=250, default='')
    created_date = models.DateTimeField(default=timezone.now)
    # approved_comment = models.BooleanField(default=False)


    
   

