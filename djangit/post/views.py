from django.shortcuts import render, redirect
from djangit.comment.form import CommentForm
from djangit.post.form import PostForm
from djangit.post.models import Post
from django.views import View
from djangit.comment.models import Comment
from djangit.subdjangit.models import Subdjangit


class CommentonPost(View):
    # we don't want the id of the comment but we want the id of the post
    """Creates a post under to current Subdjangit Community"""
    form_class = CommentForm
# We need to see the original post and all the current comments on it
# It's not showing all the comment on the post
# Not showing date created

    def get(self, request, url, id):
        form = self.form_class()
        html = "post.html"
        post_to_comment_on = Post.objects.get(id=id)

        comments = Comment.objects.filter(post=post_to_comment_on)
        return render(request, html, {"form": form, "comments": comments, "post_to_comment_on": post_to_comment_on, "id": id})

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
