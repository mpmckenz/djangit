from django import forms


class SubdjangitForm(forms.Form):
    title = forms.CharField(max_length=25)
    about = forms.CharField(max_length=50)
