from django import forms
from django.conf import settings

from ..models import Post

from .utils import WidgetClassForm


class PostForm(WidgetClassForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'url_name', 'version', 'lang', 'publish_date', 'thumbnail', 'thumbnail_caption', 'content', 'published')

    widget_additional_classes = {
        'author': 'form-select',
        'title': 'form-control',
        'url_name': 'form-control',
        'version': 'form-control',
        'lang': 'form-select',
        'thumbnail': 'form-control',
        'published': 'form-check-input',
        'publish_date': 'form-control',
    }
