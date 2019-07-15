from django.urls import path
from djangit.comment.models import Comment
from django.contrib import admin

admin.site.register(Comment)


urlpatterns = [
    path("comment/", add_comment_to_post.as_view(), name="comments")
]