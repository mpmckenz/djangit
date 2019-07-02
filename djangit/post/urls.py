from django.contrib import admin
from django.urls import path
from djangit.post.models import Post
from djangit.post.views import MyPost

admin.site.register(Post)

urlpatterns = [
    path("post/", MyPost.as_view())
]
