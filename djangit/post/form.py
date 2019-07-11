from django import forms
from djangit.post.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = {'title', 'text'}
    # title = forms.CharField(max_length=30)
    # body = forms.CharField(max_length=200)
    # url = forms.URLField(max_length=200, required=False)
