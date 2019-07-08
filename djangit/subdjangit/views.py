from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from djangit.user.models import DjangitUser
from djangit.subdjangit.models import Subdjangit


class SubdjangitList(View):
    """View to see all of the subdjangits"""

    def get(self, request):
        html = "subdjangit.html"
        subdjangits = Subdjangit.objects.all().order_by("title")
        return render(request, html, {"subdjangits": subdjangits})


class SingleSubdjangit(View):
    """View for one subdjangit"""

    def get(self, request):
        html = "subdjangit.html"
        subdjangit = Subdjangit.objects.filter(id=id)
        return render(request, html, {"subdjangit": subdjangit})

    pass