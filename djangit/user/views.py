from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from djangit.user.models import DjangitUser
from djangit.post.models import Post
from djangit.subdjangit.models import Subdjangit
from djangit.comment.models import Comment


@method_decorator(login_required, name='dispatch')
class Homepage(View):
    """View logged in user homepage"""

    def get(self, request):
        html = 'homepage.html'
        all_users = DjangitUser.objects.all()
        active_user = request.user.djangituser
        currently_moderatoring = Subdjangit.objects.filter(
            moderator=active_user)

        joined_subdjangits = active_user.subscriptions.all()

        posts = Post.objects.filter(
            subdjangit__in=joined_subdjangits).order_by('-date_created')

        data = {"all_users": all_users,
                "joined_subdjangits": joined_subdjangits,
                "currently_moderatoring": currently_moderatoring,
                "posts": posts, }
        return render(request, html, data)


class AllUsers(View):
    """Returns a list of all users"""

    def get(self, request):
        html = 'allusers.html'
        all_users = DjangitUser.objects.all()
        return render(request, html, {"all_users": all_users})


class ViewSpecificUserHomepage(View):
    """User can view other user pages"""

    def get(self, request, username):
        html = "viewspecificuserhomepage.html"
        specific_user = DjangitUser.objects.filter(username=username).first()
        other_user_posts = Post.objects.filter(user_id=specific_user)
        data = {"specific_user": specific_user,
                "other_user_posts": other_user_posts}
        return render(request, html, data)


class ToggleSubscription(View):
    """User can toggle joining subdjangit community"""

    def get(self, request, url):
        subdjangit = Subdjangit.objects.filter(url=url).first()
        active_user = request.user.djangituser
        if subdjangit not in active_user.subscriptions.all():
            active_user.subscriptions.add(
                subdjangit
            )
            return redirect("/r/{}".format(url))
        else:
            active_user.subscriptions.remove(
                subdjangit
            )
            return redirect("/")


class DeletePost(View):
    """moderator of a subdjangit can delete posts"""

    def get(self, request, id, url):
        active_user = request.user.djangituser
        moderator = Subdjangit.objects.filter(moderator=active_user)
        if moderator:
            Post.objects.filter(id=id).delete()
        return redirect("/r/{}".format(url))


class DeleteComment(View):
    """moderator of a subdjangit can delete comments on a post"""

    def get(self, request, cid, url, id):
        active_user = request.user.djangituser
        moderator = Subdjangit.objects.filter(moderator=active_user)
        if moderator:
            Comment.objects.filter(id=cid).delete()
        return HttpResponseRedirect(reverse("commentonpost", args=(url, id)))


class DeleteSubdjangit(View):
    """Deletes subdjangit if logged in user is moderator"""

    def delete(self, request, subdjangit):
        subdjangit = Subdjangit.objects.filter(title=subdjangit)
        subdjangit.delete()
        return HttpResponseRedirect('/')
