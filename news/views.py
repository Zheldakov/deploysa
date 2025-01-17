from django.views.generic import ListView

from news.models import Article


class NewsListView(ListView):
    """Список всех статей"""
    model = Article
    paginate_by = 6
    template_name = 'news/news_list.html'
    extra_context = {
        'title': f'Новости'
    }
