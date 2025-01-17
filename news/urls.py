from django.urls import path

from news.apps import NewsConfig
from news.views import NewsListView

app_name = NewsConfig.name

urlpatterns = [
    path('', NewsListView.as_view(), name="news_list"),  # список всех новостей
]