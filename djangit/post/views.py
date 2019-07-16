from django.shortcuts import render, redirect
from djangit.comment.form import CommentForm
from djangit.post.form import PostForm
from django.views import View
from djangit.comment.models import Comment
from djangit.subdjangit.models import Subdjangit


class CommentonPost(View):

    # a get to filter out that specific post id and stuff; 
    # def post in the post class what we need to create the comment
    #somewhat like the singlesubjangit
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

    def post(self, request, id, url):
        html = "post.html"
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                user=request.user.djangituser,
                url='{}'.format(url),
                text=data['text'],
                # id='{}'.format(id),
                

            )
            return redirect('/r/{}/post/{}'.format(url, id))




