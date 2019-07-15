from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from djangit.comment.form import CommentForm


def add_comment_to_post(request, pk):
   post= get_object_or_404(Post, pk=pk)
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
          comment = form.save(commit=False)
          comment.post= post
          comment.user = request.user
          comment.save()
          return redirect('postform.html', slug=post.slug)
   else:
       form = CommentForm()
   return render(request, 'comment.html', {'form':form})


