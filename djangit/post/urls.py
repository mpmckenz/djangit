from django.urls import path
from django.conf.urls import url,include
from djangit.post.models import Post
from djangit.post.views import MyPost
from django.contrib import admin

admin.site.register(Post)



urlpatterns = [
    path("post/", MyPost.as_view()),
]
