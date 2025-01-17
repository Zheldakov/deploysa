from django.db import models

# настройка полей, чтобы возможно было заполнить поля пустыми
from users.models import NULLABLE

class Article(models.Model):
    """Статья"""
    title = models.CharField(max_length=100, verbose_name='Название', **NULLABLE)  # `Название новости
    description = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)  # Описание
    date = models.DateField(verbose_name='Дата публикации')
    text = models.TextField(verbose_name="Текст статьи")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'