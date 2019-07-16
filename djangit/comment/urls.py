from django.urls import path
from djangit.comment.models import Comment
from django.contrib import admin
from django.conf.urls import url, include
from djangit.comment.views import Add_comment_to_post



admin.site.register(Comment)


urlpatterns = [
    path("comment/<int:id>", Add_comment_to_post.as_view(), name='comment')
]