from django import forms
from django.forms import widgets
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author' ,'title' ,'body', 'status', 'category']
        widgets ={
            'author': forms.HiddenInput()
        }