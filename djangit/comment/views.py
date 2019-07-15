from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from djangit.comment.form import CommentForm


class Add_comment_to_post(request):
    """Add a comment to post from a Subdjangit Community"""
    form_class = CommentForm()

    def get(self, request):
        form = self.form_class()
        return render(request, 'comment.html' {'form': form})

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


