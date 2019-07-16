from django.shortcuts import render, redirect
from djangit.comment.form import CommentForm
from djangit.post.form import PostForm
from djangit.post.models import Post
from django.views import View
from djangit.comment.models import Comment
from djangit.subdjangit.models import Subdjangit


class CommentonPost(View):
    #we don't want the id of the comment but we want the id of the post
    """Creates a post under to current Subdjangit Community"""
    form_class = CommentForm

    def get(self, request, url, id):
        form = self.form_class()
        html = "post.html"
        subdjangit = Subdjangit.objects.filter(url=url)
        active_user = request.user.djangituser
        moderator = Subdjangit.objects.all().filter(moderator=active_user)
        subdjangit_posts = Subdjangit.objects.filter(id=id)
        comments = Comment.objects.all().filter(id=id)
        
        return render(request, html, {"subdjangit": subdjangit, "form": form, "comments": comments})

    def post(self, request, url, id):
        html = "post.html"
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                user=request.user.djangituser,
                text=data['text'],
                post=Post.objects.get(id=id)
                

            )
            return redirect('/r/{}/post/{}'.format(url, id))




