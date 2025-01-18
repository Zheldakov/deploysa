from django.urls import path

from news.apps import NewsConfig
from news.views import NewsListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView

app_name = NewsConfig.name

urlpatterns = [
    path('', NewsListView.as_view(), name="news_list"),  # список всех новостей
    path('<int:pk>',ArticleDetailView.as_view(), name="news_detail"), # статья
    path('create/',ArticleCreateView.as_view(), name="news_create"), # создание статьи
    path('update/<int:pk>/',ArticleUpdateView.as_view(), name="news_update"), # редактирование статьи
    path('delete/<int:pk>',ArticleDeleteView.as_view(), name="news_delete"), # удаление статьи
]