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


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


class SubdjangitList(View):
    """View to see all of the subdjangits"""

    def get(self, request):
        html = "subdjangit.html"
        subdjangits = Subdjangit.objects.all().order_by("title")
        return render(request, html, {"subdjangits": subdjangits})


class SingleSubdjangit(View):
    """View for one subdjangit"""

    def get(self, request, url):
        form = PostForm()
        html = "singleSubdjangit.html"
        subdjangit = Subdjangit.objects.filter(url=url)

        active_user = request.user.djangituser
        moderator = Subdjangit.objects.filter(moderator=active_user)

        subdjangit_posts = Subdjangit.objects.filter(url=url)
        posts = Post.objects.filter(url=url)

        return render(request, html, {"subdjangit": subdjangit, "form": form, "posts": posts, "moderator": list(moderator)})

    def post(self, request, url):
        html = "singleSubdjangit.html"
        form = PostForm(request.POST)
        if "upvote" in request.POST:
            post_thing = int(request.POST.get("upvote"))
            post = Post.objects.get(id=post_thing)
            result = post.votes.up(request.user.id)
            if not result:
                post.votes.delete(request.user.id)
            return redirect('/r/{}'.format(url))
        elif "downvote" in request.POST:
            post_thing = int(request.POST.get("downvote"))
            post = Post.objects.get(id=post_thing)
            result = post.votes.down(request.user.id)
            if not result:
                post.votes.delete(request.user.id)
            return redirect('/r/{}'.format(url))
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                user=request.user.djangituser,
                url='{}'.format(url),
                title=data['title'],
                body=data['body'],
                subdjangit=Subdjangit.objects.get(url=url),
            )
            return redirect('/r/{}'.format(url))


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
            if Subdjangit.objects.filter(title=data['title']):
                return render(request, "cannotcreatesubdjangit.html", {"form": form})
            else:
                if " " not in data['url']:
                    Subdjangit.objects.create(
                        moderator=request.user.djangituser,
                        url=data['url'],
                        title=data["title"],
                        about=data["about"],
                    )
                    return HttpResponseRedirect('/r/{}/'.format(data['url']))
                else:
                    return render(request, "cannotcreatesubdjangit.html", {"form": form})
