from django import forms

from news.models import Article


class ArticleForm(forms.ModelForm):
    """ Форма статьи."""

    class Meta:
        model = Article
        fields = ['title', 'description', 'text']
        widgets = {
            'description': forms.Textarea(attrs={
                'cols': 65, 'rows': 5,
                'class': 'text_article_form'}),
            'text': forms.Textarea(attrs={
                # 'cols': 65, 'rows': 20,
                'class': 'text_article_form'}),
        }
