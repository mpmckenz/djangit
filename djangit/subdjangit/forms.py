from django import forms


class SubdjangitForm(forms.Form):
    title = forms.CharField(max_length=50)
    url = forms.CharField(max_length=50)
    about = forms.CharField(max_length=75)
