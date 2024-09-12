from django import forms
from .models import Comment Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'TagWidget()', 'widgets']

