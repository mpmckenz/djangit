from django.shortcuts import render
from django.views import View

from redjit.redjituser.forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from redjit.redjituser.models import RedjitUser
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse
from django.http import HttpResponseRedirect


# Create your views here.
class SignUp(View):
    html = 'signupform.html'

    def get(self, request):
        form = SignupForm()
        return render(request, self.html, {'form': form})

    def post(self, request):
        form = None
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                # django 'User' built-in model
                user = User.objects.create_user(
                    username=data['username'],
                    password=data['password'],
                )
                user.save()
                # Actual Redjit user that can post and stuff
                RedjitUser.objects.create(
                    user=user,
                    password=data['password']
                )
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))


class Login(View):
    html = 'loginform.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.html, {'form': form})

    def post(self, request):
        form = None
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(
                    username=data['username'],
                    password=data['password']
                )
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get("next", "/"))


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("homepage"))


class Index(View):
    def get(self, request):
        html = 'index.html'

        return render(request, html)
