from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from djangit.user.models import DjangitUser
from djangit.subdjangit.models import Subdjangit
from djangit.subdjangit.forms import SubdjangitForm


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
        html = "singleSubdjangit.html"
        subdjangit = Subdjangit.objects.filter(url=url)
        # do as pass in for the count of the subscribers
        return render(request, html, {"subdjangit": subdjangit})


class CreateSubdjangit(View):
    """Creates a subdjangit or if it already exists, redirects to that subdjangit"""

    def get(self, request):
        html = "createSubdjangitform.html"
        form = SubdjangitForm()
        return render(request, html, {'form': form})

    def post(self, request):
        form = SubdjangitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if Subdjangit.objects.filter(url=data['url']):
                return HttpResponseRedirect('r/{}/'.format(data['url']))
            else:
                if " " not in data['url']:
                    Subdjangit.objects.create(
                        moderator=request.user.djangituser,
                        url=data['url'],
                        title=data["title"],
                        about=data["about"],
                    )
                    return HttpResponseRedirect('/')


class DeleteSubdjangit(View):
    """Deletes subdjangit if logged in user is moderator"""

    def delete(self, request, subdjangit):
        subdjangit = Subdjangit.objects.filter(title=subdjangit)
        subdjangit.delete()
        return HttpResponseRedirect('/')
