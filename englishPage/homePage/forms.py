from django import forms
from .models import PostModel
from .models import DictionaryModel


class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title_book', 'content_book', 'translate_book')

class PostDictionaryForm(forms.ModelForm):
    class Meta:
        model = DictionaryModel
        fields = ('user', 'translate_book')