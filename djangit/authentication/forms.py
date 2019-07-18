from django import forms
from djangit.user.models import DjangitUser


class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.ModelForm):
    class Meta: 
        model = DjangitUser
        fields = ["username", "password"]
        # username = forms.CharField(max_length=50)
        # password = forms.CharField(widget=forms.PasswordInput())
