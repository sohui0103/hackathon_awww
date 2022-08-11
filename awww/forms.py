from django import forms
from awww.models import Blog, Comment

class BlogUpdate(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']