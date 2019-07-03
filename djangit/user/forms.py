from django import forms
# from models import RedjitUser


class SignupForm(forms.Form):
    # https://stackoverflow.com/questions/17523263/how-to-create-password-field-in-model-django
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    # user = forms.CharField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
