from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from ..models import Post, Comment, Quote
from martor.widgets import AdminMartorWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'version', 'lang', 'thumbnail', 'thumbnail_caption', 'content', 'published')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'version': forms.TextInput(attrs={'class': 'textinputclass'}),
            'lang': forms.TextInput(attrs={'class': 'textinputclass'}),
            'thumbnail': forms.FileInput(attrs={'class': 'textinputclass'}),
            'thumbnail_caption': forms.FileInput(attrs={'class': 'textinputclass'}),
            'content': AdminMartorWidget(),
            'published': forms.CheckboxInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable tinymce-editor'}),
        }


class QuoteForm(forms.ModelForm):

    recaptcha = ReCaptchaField(widget=ReCaptchaV3(action='quote'))

    class Meta:
        model = Quote
        fields = ('author', 'email', 'phone', 'company', 'quote',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'quote': forms.Textarea(attrs={'class': 'form-control'}),
        }
