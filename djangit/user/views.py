from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from djangit.user.models import DjangitUser


@method_decorator(login_required, name='dispatch')
class Homepage(View):
    """View logged in user homepagethird argument in render() is the data we want to pass to the template"""

    def get(self, request):
        html = 'homepage.html'
        # logged_in_user_details = DjangitUser.objects.filter(
        #     username=request.user.djangituser).first()

        # list_of_followed_usernames = logged_in_user_details.following.all()

        # followed_user_posts = DjangitUser.objects.filter(
        # username=username).first()

        # data = {'followed_user_posts': followed_user_posts,
        # 'logged_in_user_details': logged_in_user_details, 'list_of_followed_usernames': list_of_followed_usernames}

        return render(request, html)
