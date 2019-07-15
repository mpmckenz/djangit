from django import forms
from djangit.comment.models import Comment


class CommentForm(forms.Form):
        model = Comment
        fields = ['post', 'user', 'text', 'created_date']