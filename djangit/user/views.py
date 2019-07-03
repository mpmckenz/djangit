from django.shortcuts import render
from django.views import View

from django.shortcuts import render


class Profile(View):
    def get(self, request):
        html = 'profile.html'

        return render(request, html)
