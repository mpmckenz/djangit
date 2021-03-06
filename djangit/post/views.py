from django.shortcuts import render, redirect
from djangit.comment.form import CommentForm
from djangit.post.form import PostForm
from djangit.post.models import Post
from django.views import View
from djangit.comment.models import Comment
from djangit.subdjangit.models import Subdjangit


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


class CommentonPost(View):
    """Creates a post under to current Subdjangit Community"""
    form_class = CommentForm

    def get(self, request, url, id):
        form = self.form_class()
        html = "post.html"
        post_to_comment_on = Post.objects.get(id=id)

        active_user = request.user.djangituser
        moderator = Subdjangit.objects.filter(moderator=active_user)

        comments = Comment.objects.filter(post=post_to_comment_on)
        return render(request, html, {"form": form, "comments": comments, "post_to_comment_on": post_to_comment_on, "id": id, "moderator": moderator})

    def post(self, request, url, id):
        html = "post.html"
        form = self.form_class(request.POST)
        if "upvote" in request.POST:
            comment_thing = int(request.POST.get("upvote"))
            comment = Comment.objects.get(id=comment_thing)
            result = comment.votes.up(request.user.id)
            if not result:
                comment.votes.delete(request.user.id)
            return redirect('/r/{}/post/{}'.format(url, id))
        elif "downvote" in request.POST:
            comment_thing = int(request.POST.get("downvote"))
            comment = Comment.objects.get(id=comment_thing)
            result = comment.votes.down(request.user.id)
            if not result:
                comment.votes.delete(request.user.id)
            return redirect('/r/{}/post/{}'.format(url, id))
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                user=request.user.djangituser,
                text=data['text'],
                post=Post.objects.get(id=id)
            )
            return redirect('/r/{}/post/{}'.format(url, id))
