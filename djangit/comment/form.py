from django.forms import ModelForm
from djangit.comment.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']