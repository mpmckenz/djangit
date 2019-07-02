from django.shortcuts import render
from django.views import View

from django.shortcuts import render

# Create your views here.
class Index(View):
    def get(self, request):
        html = 'index.html'
        
        return render(request, html)