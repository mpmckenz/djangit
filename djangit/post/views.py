from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from djangit.post.form import PostForm
from .models import Post
from djangit.post.helper import toggle_comment_upvotes
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


class SubDjangitView(View):

    form_class = PostForm

    def get(self, request, subdjangit):
        response = {}
        form = self.form_class()
        # html = #whatever you name the html page for it
        sub = SubDjangit.objects.filter(title=subdjangit).first()
        posts = sort_posts(Post.objects.filter(subdjangit=sub).all())
        response.update({"sub": sub, "form": form,
                         "posts": posts,
        })
                        
        return render(request, html, response)

    