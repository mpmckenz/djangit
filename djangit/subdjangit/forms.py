from django import forms


class SubdjangitForm(forms.Form):
    title = forms.CharField(max_length=25)
    url = forms.CharField(max_length=50)
    about = forms.TextField(max_length=50)
