from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from djangit.user.models import DjangitUser


class SubdjangitList(View):
    """View logged in user homepagethird argument in render() is the data we want to pass to the template"""

    def get(self, request):
        html = 'subdjangit.html'
        return render(request, html)

    def post(self, request):
        pass