from django.shortcuts import render, reverse, HttpResponseRedirect
from .form import SubdjangitForm
from djangit.post.form import PostForm
from djangit.post.models import Post
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from djangit.user.models import DjangitUser
from djangit.subdjangit.models import Subdjangit
from djangit.subdjangit.form import SubdjangitForm


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

    def get(self, request):
        html = "subdjangit.html"
        subdjangit = Subdjangit.objects.filter(id=id)
        return render(request, html, {"subdjangit": subdjangit})

    pass