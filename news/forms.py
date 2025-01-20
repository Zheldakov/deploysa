from django import forms

from news.models import Article



class ArticleForm(forms.ModelForm):
    """ Форма статьи."""

    class Meta:
        model = Article
        fields = ['title', 'description', 'text']
