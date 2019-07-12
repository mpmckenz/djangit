from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from djangit.post.form import PostForm
from .models import Post
from djangit.post.helper import toggle_comment_upvotes
from django.views import View


class MyPost(View):
    """Creates a post under to current Subdjangit Community"""
    form_class = PostForm()

    def get(self, request, *args):
        form = self.form_class
        return render(request, 'postform.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                title=data['title'],
                body=data['data']
            )
            return redirect('/r/<str:url>/')
