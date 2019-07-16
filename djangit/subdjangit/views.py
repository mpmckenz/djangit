from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from djangit.user.models import DjangitUser
from djangit.subdjangit.models import Subdjangit
from djangit.subdjangit.forms import SubdjangitForm

from djangit.post.form import PostForm
from djangit.post.models import Post


class SubdjangitList(View):
    """View to see all of the subdjangits"""

    def get(self, request):
        html = "subdjangit.html"
        subdjangits = Subdjangit.objects.all().order_by("title")
        return render(request, html, {"subdjangits": subdjangits})

   



    #creating the option to post in the community and see all posts that have been made and then 
    #click on the post which leads to a different template and begins the thread. 



class SingleSubdjangit(View):
    """View for one subdjangit"""

    def get(self, request, url):
        form = PostForm()
        html = "singleSubdjangit.html"
        subdjangit = Subdjangit.objects.filter(url=url)

        active_user = request.user.djangituser
        moderator = Subdjangit.objects.all().filter(moderator=active_user)

        subdjangit_posts = Subdjangit.objects.filter(url=url)
        posts = Post.objects.all().filter(url=url)

        return render(request, html, {"subdjangit": subdjangit, "form": form, "posts": posts, "moderator": list(moderator)})

    def post(self, request, url):
        html = "singleSubdjangit.html"
        # path_info = request.META.get('PATH_INFO')
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                user=request.user.djangituser,
                url='{}'.format(url),
                title=data['title'],
                body=data['body'],
            )
            subdjangit_posts = Subdjangit.objects.filter(url=url)
            posts = Post.objects.all()
            # I want the page to stay on the subdjangit community
            return redirect('/r/{}'.format(url))
            # return render(request, '/r/{}'.format(url), {"posts": posts})

    def post_new(self, request):
        if request.method == 'POST':
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('singleSubdjangit.html', pk=post.pk)
        else:
            form = PostForm
        return render(request, "singleSubdangit.html", {'form': form})

    # def comment_new(self, request):
    #     if request.method == 'POST':
    #         if form.is_valid():
    #             comment = form.save(commit=False)
    #             comment.save()
    #             return redirect('comment.html', pk=comment.pk)
    #     else:
    #         form = CommentForm
    #     return render(request, "comment.html", {'form': form} )
        


class CreateSubdjangit(View):
    """Creates a subdjangit or if it already exists, redirects to that subdjangit"""

    def get(self, request):
        html = "createSubdjangitForm.html"
        form = SubdjangitForm()
        return render(request, html, {'form': form})

    def post(self, request):
        form = SubdjangitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if Subdjangit.objects.filter(url=data['url']):
                return HttpResponseRedirect('/r/{}/'.format(data['url']))
            else:
                if " " not in data['url']:
                    Subdjangit.objects.create(
                        moderator=request.user.djangituser,
                        url=data['url'],
                        title=data["title"],
                        about=data["about"],
                    )
                    return HttpResponseRedirect('/')


# class DeleteSubdjangit(View):
#     """Deletes subdjangit if logged in user is moderator"""

#     def delete(self, request, subdjangit):
#         subdjangit = Subdjangit.objects.filter(title=subdjangit)
#         subdjangit.delete()
#         return HttpResponseRedirect('/')
