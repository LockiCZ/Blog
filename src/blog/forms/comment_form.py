from django import forms
from ..models import Comment

from .utils import WidgetClassForm


class CommentForm(WidgetClassForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable tinymce-editor'}),
        }
