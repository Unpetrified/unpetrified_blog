from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'content', 'photo']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'text', 'placeholder' : 'Enter the title of this piece',}),
            'content' : forms.Textarea(attrs={'class' : 'content', 'placeholder' : 'Go on...be creative'}),
            'photo' : forms.FileInput(attrs={'class' : 'file'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = ['comment_body']
        widgets = {
            'comment_body' : forms.TextInput(attrs={'class':'comment-body'})
        }