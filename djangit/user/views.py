from django.shortcuts import render
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
        # logged_in_user_details = DjangitUser.objects.filter(
        #     username=request.user).first()

        all_users = DjangitUser.objects.all()

        # sortby_highest_voted_posts = Post.objects.all().order_by('-upvotes')

        # sortby_lowest_voted_posts = Post.objects.all().order_by('-downvotes')

        # sortby_newest_posts = Post.objects.all().order_by('-date_created')

        # list_of_followed_usernames = logged_in_user_details.following.all()

        # followed_user_posts = DjangitUser.objects.filter(
        #     username=username).first()

        # data = {'followed_user_posts': followed_user_posts,
        # 'logged_in_user_details': logged_in_user_details, 'list_of_followed_usernames': list_of_followed_usernames}
        data = {"all_users": all_users}
        return render(request, html, data)


class ViewSpecificUserHomepage(View):
    def get(self, request, username):
        html = "viewspecificuserhomepage.html"
        specific_user = DjangitUser.objects.filter(username=username).first()
        other_user_posts = Post.objects.filter(user_id=specific_user)
        data = {"specific_user": specific_user,
                "other_user_posts": other_user_posts}
        return render(request, html, data)


class SubscribeToSubdjangit(View):
    def get(self, request, subdjangit):
        subdjangit = DjangitUser.objects.filter(
            subdjangit=subdjangit).first()
        if subdjangit not in request.user.subscriptions.get_queryset():
            request.user.subscriptions.add(subdjangit)
        else:
            request.user.following.remove(subdjangit)
        request.user.save()
        return redirect("/{}/".format(subdjangit))
