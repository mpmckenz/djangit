from django.shortcuts import render, redirect
from django.http import HttpResponse
from djangit.comment.form import CommentForm
from djangit.comment.models import Comment
from django.views import View


class Add_comment_to_post(View):
    """Add a comment to post from a Subdjangit Community"""
    form_class = CommentForm()

    def get(self, request):
        form = self.form_class()
        return render(request, 'comment.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Comment.objects.create(
                    text=data['text']
                )
            return redirect('/comment/')
        else:
            form = CommentForm()
        return render(request, 'comment.html', {'form': form})
