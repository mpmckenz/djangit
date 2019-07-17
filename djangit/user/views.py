from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from djangit.user.models import DjangitUser
from djangit.post.models import Post
from djangit.subdjangit.models import Subdjangit


@method_decorator(login_required, name='dispatch')
class Homepage(View):
    """View logged in user homepagethird argument in render() is the data we want to pass to the template"""

    def get(self, request):
        html = 'homepage.html'
        # all user button
        all_users = DjangitUser.objects.all()

        active_user = request.user.djangituser

        currently_moderatoring = Subdjangit.objects.filter(
            moderator=active_user)
        active_user_posts = Post.objects.filter(
            user=active_user).order_by('-date_created')

        all_subdjangits = Subdjangit.objects.all()
        active_user_subdjangit_title = []
        for sub_title in all_subdjangits:
            active_user_subdjangit_title = Subdjangit.objects.filter(
                url=sub_title)

        joined_subdjangits = active_user.subscriptions.all()
        for community in joined_subdjangits:
            joined_subdjangit_posts = Post.objects.filter(
                url=community)
            subdjangit_title = Subdjangit.objects.filter(url=community)
        # sortby_highest_voted_posts = Post.objects.all().order_by('-upvotes')

        # sortby_lowest_voted_posts = Post.objects.all().order_by('-downvotes')

        # sortby_newest_posts = Post.objects.filter(
        #     user=active_user).order_by('-date_created')

        # list_of_followed_usernames = logged_in_user_details.following.all()

        # followed_user_posts = DjangitUser.objects.filter(
        #     username=username).first()

        data = {"joined_subdjangits": joined_subdjangits,
                "currently_moderatoring": currently_moderatoring, "active_user_posts": active_user_posts, "joined_subdjangit_posts": joined_subdjangit_posts, "subdjangit_title": subdjangit_title, "active_user_subdjangit_title": active_user_subdjangit_title}
        return render(request, html, data)

    # {% for item in active_user_posts %}
    # <div class="card">
    #   {% for user_community in active_user_subdjangit_title %}
    #   <a href="">{{ user_community.title }}</a>
    #   {% endfor %}
    #   <br />
    #   <a href="/user/{{ item.user }}">{{ item.user }}</a>
    #   <p>{{ item.date_created }}</p>
    #   <p>
    #     <b>{{ item.title }}</b>
    #   </p>
    #   <p>
    #     <i>{{ item.body }}</i>
    #   </p>
    # </div>


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


class DeleteSubdjangit(View):
    """Deletes subdjangit if logged in user is moderator"""

    def delete(self, request, subdjangit):
        subdjangit = Subdjangit.objects.filter(title=subdjangit)
        subdjangit.delete()
        return HttpResponseRedirect('/')
