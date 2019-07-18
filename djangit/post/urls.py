from django.urls import path
from django.conf.urls import url, include
from djangit.post.models import Post
from djangit.comment.models import Comment
from djangit.post.views import CommentonPost
from django.contrib import admin

admin.site.register(Comment)
admin.site.register(Post)


urlpatterns = [
    path("r/<str:url>/post/<int:id>/",
         CommentonPost.as_view(), name='commentonpost')
]
