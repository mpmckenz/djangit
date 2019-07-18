from django.shortcuts import render

from djangit.user.models import DjangitUser
from djangit.authentication.forms import SignupForm, LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.views import View


class SignUp(View):
    html = 'signupform.html'

    def get(self, request):
        form = SignupForm()
        return render(request, self.html, {"form": form})

    def post(self, request):
        badsignup_username = 'badsignupusername.html'
        badsignup_email = 'badsignupemail.html'
        form = None
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                if User.objects.filter(username=data['username']):
                    return render(request, badSignup_username)
                if User.objects.filter(email=data['email']):
                    return render(request, badsignup_email)
                else:
                    user = User.objects.create_user(
                        username=data["username"],
                        email=data["email"],
                        password=data["password"],
                    )
                    user.save()
                    DjangitUser.objects.create(
                        user=user,
                        username=data['username'],
                        password=data["password"],
                        email=data["email"],
                    )
                    login(request, user)
                    return HttpResponseRedirect(reverse("homepage"))


class Login(View):
    html = "loginform.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.html, {"form": form})

    def post(self, request):
        form = None
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(
                    username=data["username"], password=data["password"])
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get("next", "/"))


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("homepage"))
