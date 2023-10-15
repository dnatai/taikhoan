from django import forms
from .models import Post, Comment

class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'elder', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }

class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' ,'type':'hidden', 'value':'','id':'tai'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),     
        }