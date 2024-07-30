from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']