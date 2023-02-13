from django import forms
from django.forms import ModelForm
from .models import Post, Tag, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['writer','slug']



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['post',]