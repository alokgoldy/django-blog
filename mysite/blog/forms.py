from django import forms
from models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.TextArea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class ComentForm(forms.ModelForm):

    class Meta():
        model = comment
        fields = ('author','text')

        widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.TextArea(attrs={'class':'editable medium-editor-textarea'})
        }
