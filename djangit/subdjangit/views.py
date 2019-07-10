<<<<<<< HEAD
from django.shortcuts import render, reverse, HttpResponseRedirect
from .form import SubdjangitForm
from djangit.post.form import PostForm
from djangit.post.models import Post
=======
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

>>>>>>> 3a9dfddb703819e4132969454634398316da5aa9
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from djangit.user.models import DjangitUser
from djangit.subdjangit.models import Subdjangit
<<<<<<< HEAD
from djangit.subdjangit.form import SubdjangitForm
=======
from djangit.subdjangit.forms import SubdjangitForm
>>>>>>> 3a9dfddb703819e4132969454634398316da5aa9


class CreateNewSub(View):
    """View to see all of the subdjangits"""

    form_class = SubdjangitForm

    def get(self, request):
        response = {}
        form = self.form_class()
        response.update({"form": form})
        all_subs = DjangitUser.objects.all()
        response.update({"all_subs": all_subs})
        return render(request, "./createnewsub.html", response)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid() and hasattr(request.user, 'djangituser'):
            data = form.cleaned_data
            Subdjangit.objects.create(
                creator=request.user.subjangit,
                title=data['title'].replace(" ", ""),
                about=data['about'],
            )
            return HttpResponseRedirect(reverse("subdjangits"))
        form = self.form_class()
        return render(request, "./createnewsub.html", {"form": form})


class SingleSubdjangit(View):
    """View for one subdjangit"""

    def get(self, request, title):
        html = "singleSubdjangit.html"
        subdjangit = Subdjangit.objects.filter(title=title).first()
        # do as pass in for the count of the subscribers
        return render(request, html, {"subdjangit": subdjangit})


class CreateSubdjangit(View):
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
