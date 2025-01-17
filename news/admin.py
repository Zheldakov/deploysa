from django.contrib import admin

from news.models import Article


# Модель Article в административной панели Django
@admin.register(Article)
class UserAdmin(admin.ModelAdmin):
    """Отображение в админ панели новостной статьи"""
    list_display = ('id','title','description','date') # Показываем поля в списке модели
    list_filter = ('id','date') # Фильтрация
    ordering = ('id',)
