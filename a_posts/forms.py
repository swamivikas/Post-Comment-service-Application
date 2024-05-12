from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url','body']
        labels = {
            'body': 'Captions',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows':3, 'placeholder':'Add a Caption...', 'class':'font1 text-4xl'}),
            'url': forms.TextInput(attrs={ 'placeholder':'Add url...'}),

        }


class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body' : '',

        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),

        }
   
   
class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Add comment ...'})
        }
        labels = {
            'body': ''
        }
        
             