from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from djangit.post.form import PostForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from djangit.user.models import DjangitUser
from djangit.subdjangit.models import Subdjangit
from djangit.subdjangit.forms import SubdjangitForm

class SubdjangitList(View):
    """View to see all of the subdjangits"""

    form_class = PostForm

    def get(self, request):
        request = {}
        form = self.form_class()
        html = "subdjangit.html"
        sub = Subdjangit.objects.all().order_by("title")
        posts = sort_posts(Post.objects.filter(subdangit=sub).all())
        response.update({"sub": sub, "form": form,
                        "posts": posts, })
        return render(request, html, response)

    def post(self, request):
        form = self.form_class(request.POST)
        toggle_post_upvotes(request)
        toggle_post_downvotes(request)
        if form.is_valid():
            data = form.cleaned_data
            user = DjangitUser.objects.get(pk=request.user.djangituser.pk)
            Posts.object.create(
                user = data['user'],
                title = data['title'],
                body = data['body'],
                subdjangit = Subdjangit.objects.filter(title=subdjangit).first()

            )
        return HttpResponseRedirect(reverse('subdangit', kwargs={"subdjangit": subdjangit}))


class SingleSubdjangit(View):
    """View for one subdjangit"""

    def get(self, request, title):
        html = "singleSubdjangit.html"
        subdjangit = Subdjangit.objects.filter(title=title).first()
        # do as pass in for the count of the subscribers
        return render(request, html, {"subdjangit": subdjangit})





class CreateSubdjangit(View):
    """Create a new community"""

    def get(self, request):
        html = "createSubdjangitform.html"
        form = SubdjangitForm()
        return render(request, html, {'form': form})

    def post(self, request):
        form = SubdjangitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if Subdjangit.objects.filter(title=data['title']):
                return HttpResponseRedirect(reverse('{}/'.format(data['title'])))
            else:
                Subdjangit.objects.create(
                    title=data["title"],
                    about=data["about"],
                )
                DjangitUser.objects.add(
                    moderator=request.user,
                )
                return render(request, '/')
