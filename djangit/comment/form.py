from django import forms
from djangit.comment.models import Comment


class CommentForm(forms.Form):
        text = forms.CharField(widget=forms.Textarea)