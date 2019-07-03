from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from djangit.post.forms import PostForm
from .models import Post
from djangit.post.helper import toggle_comment_upvotes, sort_comments
from django.views import View


class MyPost(View):
    form_class = PostForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'newpost.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('register'))
        form = self.form_class()
        return render(request, 'newpost.html', {'form': form})
