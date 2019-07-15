from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from djangit.comment.form import CommentForm
from djangit.post.form import PostForm

from django.views import View


class MyPost(View):
    """Creates a post under to current Subdjangit Community"""
    form_class = PostForm()

    def get(self, request, *args):
        form = self.form_class()
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

class AddPostToComment(View):
    form_class = CommentForm

    def get(self, request, post_id):
        response = {}
        post = Post.objects.get(id=post_id)
        comments = sort_comment(post.comments_set.get_queryt())
        response.update({"post": post})
        response.update({"form": self.form_class()})
        response.update({"comments": comments})
        return render(request, "post.html", response)


    def post(self, request, post_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = data.cleaned_data
            Comment.objects.create(
                text=['text'],
                user=request.user.djangituser,
                post=Post.objects.get(id=post_id),
                )
        return HttpResponseRedirect(reverse('post',
                                            kwargs={"subdjangit": subdjangit,
                                                    "post_id": post_id}))

    # def _addposttocomment(request, post_id):
    #     try:
    #         post = Post.objects.get(id=post_id)
    #         context['post'] = post
    #         context['form'] = CommentForm()
    #         if request.method == 'POST':
    #             form = CommentForm(request.POST)
    #             if form.is_valid():
    #                 comment = form.cleaned_data['comment']
    #                 post.comments_set.create(comment=comment)
    #         return render(request, 'comment.html', context)
    #     except Exception as e:
    #         return render(request, 'comment.html', {'form': form})


        # if request.method == 'POST':
        #     form = CommentForm(request.POST)
        #     if form.is_valid():
        #         comment = form.save(commit=False)
        #         comment.save()
        #         return redirect('singleSubdjangit.html', pk=comment.pk)
        # else:
        #     form = CommentForm
        # return render(request, "singleSubdangit.html", {'form': form})

