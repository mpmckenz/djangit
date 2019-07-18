from django import forms
from djangit.post.models import Post


class PostForm(forms.Form):
    name = forms.CharField(max_length=30)
    title = forms.CharField(max_length=30)
    body = forms.CharField(widget=forms.Textarea)
    
   
