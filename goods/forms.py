from django import forms

from .models import Comment

class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']