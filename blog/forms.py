from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author' ,'title' ,'body', 'status', 'category', 'image']
        widgets ={
            'author': forms.HiddenInput()
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_cooment', 'post', 'mycomment']
        widgets = {
            'user_cooment': forms.HiddenInput()
        }