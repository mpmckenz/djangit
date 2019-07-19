from django import forms
from djangit.post.models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=30)
    body = forms.CharField(widget=forms.Textarea)
