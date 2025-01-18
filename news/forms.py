from django import forms

from news.models import Article
from users.forms import StyleFromMixin


class ArticleForm(StyleFromMixin, forms.ModelForm):
    """ Форма статьи."""

    class Meta:
        model = Article
        fields = ['title', 'description', 'text']
